from holehe.core import *
from holehe.localuseragent import *
import secrets


# FALSE

async def paavlikaltsukas(email, client, out):
  name = "paavlikaltsukas"
  domain = "paavlikaltsukas.ee"
  method = "register"
  frequent_rate_limit = False

  headers = {
    'User-Agent': random.choice(ua["browsers"]["firefox"]),
    'Accept': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': f'PHPSESSID={secrets.token_hex(16)};'
  }

  response = await client.get(
    f"https://www.paavlikaltsukas.ee/konto/kontrolli-email/{email}?async=false",
    headers=headers
  )

  if response.json().get("exists") == 1:
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
