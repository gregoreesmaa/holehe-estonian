from holehe.core import *
from holehe.localuseragent import *

# FALSE

async def flirtic(email, client, out):
  name = "flirtic"
  domain = "flirtic.ee"
  method = "register"
  frequent_rate_limit = False

  headers = {
    'User-Agent': random.choice(ua["browsers"]["firefox"]),
    'Content-Type': 'application/x-www-form-urlencoded',
  }

  data = {
    'email': email,
    'password': 'SimplePassword123!',
  }

  response = await client.post(
    "https://www.flirtic.ee/register",
    headers=headers,
    data=data
  )

  if "Aadress on juba kasutusel" in response.text:
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
