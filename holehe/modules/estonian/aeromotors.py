from holehe.core import *
from holehe.localuseragent import *

# FALSE

async def aeromotors(email, client, out):
  name = "aeromotors"
  domain = "aeromotors.ee"
  method = "register"
  frequent_rate_limit = False

  headers = {
    'User-Agent': random.choice(ua["browsers"]["firefox"]),
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://aeromotors.ee',
    'Referer': 'https://aeromotors.ee/login?back=my-account',
  }

  data = {
    "controller": "authentication",
    "SubmitCreate": "1",
    "ajax": "true",
    "email_create": email,
    "back": "my-account",
    "token": "5139522895d711759e95066d7e1106f4"
  }

  response = await client.post('https://aeromotors.ee/', headers=headers,
                               data=data)

  json_response = response.json()
  errors = json_response.get("errors", [])
  if any("konto juba registreeritud" in error for error in errors):
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
