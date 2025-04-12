import json  # Potentially useful for parsing response

from holehe.core import *
from holehe.localuseragent import *

# OK, minimised

async def cvkeskus(email, client, out):
  name = "cvkeskus"
  domain = "cvkeskus.ee"
  method = "login"
  frequent_rate_limit = False
  
  # Do an initial request to initiate session and get CSRF token
  tokens_response = await client.get("https://www.cvkeskus.ee/")
  phpsessid_value = tokens_response.cookies.get('PHPSESSID')
  match = re.search(r'<meta\s+name="csrf-token"\s+content="([^"]*)"', tokens_response.text, re.IGNORECASE)
  csrf_token_value = match.group(1)

  boundary = "----HoleheSimpleStaticBoundary98765"
  headers = {
    'Referer': 'https://www.cvkeskus.ee/login',
    'Content-Type': f"multipart/form-data; boundary={boundary}",
    'Cookie': f"PHPSESSID={phpsessid_value}"
  }

  body_string = (
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="csrf_token"\r\n\r\n'
    f'{csrf_token_value}\r\n'
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="username"\r\n\r\n'
    f"{email}\r\n"
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="password"\r\n\r\n'
    f'dummypasswordforcheck123\r\n'
    f"--{boundary}--\r\n"
  )

  response = await client.post(
    "https://www.cvkeskus.ee/login.php?op=ajax_login&newform=1",
    headers=headers,
    data=body_string.encode('utf-8')
  )
  
  if "Palun sisesta korrektne email" in response.text:
    out.append({
      "name": name,
      "domain": domain,
      "method": method,
      "frequent_rate_limit": frequent_rate_limit,
      "rateLimit": False,
      "exists": False,
      "emailrecovery": None,
      "phoneNumber": None,
      "others": None
    })
  else:
    out.append({
      "name": name,
      "domain": domain,
      "method": method,
      "frequent_rate_limit": frequent_rate_limit,
      "rateLimit": False,
      "exists": True,
      "emailrecovery": None,
      "phoneNumber": None,
      "others": None
    })
