from holehe.core import *
from holehe.localuseragent import *

# FALSE

async def err(email, client, out):
  name = "err"
  domain = "err.ee"
  method = "register"
  frequent_rate_limit = False
  
  boundary = "----HoleheSimpleStaticBoundary98765"
  headers = {
    'User-Agent': random.choice(ua["browsers"]["firefox"]),
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://jupiter.err.ee',
    'Referer': 'https://jupiter.err.ee/',
    'Content-Type': f'multipart/form-data; boundary={boundary}',
  }

  body_string = (
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="email"\r\n'
    f"\r\n"
    f"{email}\r\n"
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="pass"\r\n'
    f"\r\n"
    f"dummypasswordforcheck123\r\n"
    f"--{boundary}--\r\n"
  )

  rate_limit_detected = False

  response = await client.post(
    "https://services.err.ee/api/publicUser/validateData",
    headers=headers,
    data=body_string.encode('utf-8')
  )
  if "Selline e-posti aadress on " in response.text:
    out.append({
      "name": name,
      "domain": domain,
      "method": method,
      "frequent_rate_limit": frequent_rate_limit,
      "rateLimit": rate_limit_detected,
      "exists": True,
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
      "rateLimit": rate_limit_detected,
      "exists": False,
      "emailrecovery": None,
      "phoneNumber": None,
      "others": None
    })
