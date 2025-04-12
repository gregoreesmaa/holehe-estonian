import json

from holehe.core import *
from holehe.localuseragent import *

# OK

async def euronics(email, client, out):
  name = "euronics"
  domain = "euronics.ee"
  method = "register"
  frequent_rate_limit = False

  headers = {
    'User-Agent': random.choice(ua["browsers"]["firefox"]),
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.euronics.ee',
  }

  response = await client.post(
    'https://www.euronics.ee/Account/ValidateRegistrationEmail',
    headers=headers,
    data=json.dumps(email)
  )

  response_json = response.json()
  if response_json.get("ok") is False:
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
