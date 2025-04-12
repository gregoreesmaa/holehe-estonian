from holehe.core import *
from holehe.localuseragent import *

# OK

async def kuldnebors(email, client, out):
  name = "kuldnebors"
  domain = "kuldnebors.ee"
  method = "register"
  frequent_rate_limit = False

  boundary = "----HoleheBoundaryKuldneBors73498"

  multipart_body_string = (
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"r_user_id\"\r\n\r\n"
    f"\r\n"
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"r_filled\"\r\n\r\n"
    f"1\r\n"
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"r_mode\"\r\n\r\n"
    f"\r\n"
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"r_language_id\"\r\n\r\n"
    f"en\r\n"
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"r_firstname\"\r\n\r\n"
    f"Test\r\n"
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"r_lastname\"\r\n\r\n"
    f"User\r\n"
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"r_action\"\r\n\r\n"
    f"puser\r\n"
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"r_kb_usertype\"\r\n\r\n"
    f"puser\r\n"
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"r_email\"\r\n\r\n"
    f"{email}\r\n"
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"r_password\"\r\n\r\n"
    f"testpassword\r\n"
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"r_password2\"\r\n\r\n"
    f"testpassword\r\n"
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"r_user_agreement\"\r\n\r\n"
    f"1\r\n"
    f"--{boundary}--\r\n"
  )

  headers = {
    'User-Agent': random.choice(ua["browsers"]["firefox"]),
    'Origin': 'https://www.kuldnebors.ee',
    'Referer': 'https://www.kuldnebors.ee/minireg.mec',
    'Content-Type': f'multipart/form-data; boundary={boundary}',
  }

  response = await client.post(
    "https://www.kuldnebors.ee/minireg.mec",
    headers=headers,
    content=multipart_body_string
  )

  if "Antud e-maili aadress on juba registreeritud!" in response.text:
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
  else:
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
