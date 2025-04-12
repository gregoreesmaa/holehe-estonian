from holehe.core import *
from holehe.localuseragent import *


# TRUE

async def city24(email, client, out):
  name = "city24"
  domain = "city24.ee"
  method = "login"  # Using the token endpoint simulates a login attempt
  frequent_rate_limit = False
  headers = {
    'User-Agent': random.choice(ua["browsers"]["firefox"]),
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Origin': 'https://www.city24.ee',
    'Referer': 'https://www.city24.ee/',
    "x-anon-token": "1728221889ea1762f3-5855-426a-ba113da352b625e3"
  }

  data = {
    "username": email,
    "password": "a_dummy_password_123!",  # Any incorrect password
    "default_portal": "CITY24_EE"
  }

  response = await client.post(
    "https://api.city24.ee/token",
    headers=headers,
    json=data
  )

  if "Username could not be found." in response.text:
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
