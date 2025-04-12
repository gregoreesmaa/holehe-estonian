from holehe.core import *
from holehe.localuseragent import *


# FALSE

async def forum(email, client, out):
  name = "forum"
  domain = "forum.ee"
  method = "register"
  frequent_rate_limit = False

  # Static secure_key obtained manually, based on the JS snippet.
  # Note: If this check stops working, this static key might need updating.
  secure_key_value = "880ea6a14ea49e853634fbdc5015a024"

  headers = {
    'User-Agent': random.choice(ua["browsers"]["firefox"]),
    'Accept': 'application/json, text/plain, */*',  # Expecting JSON response
    'Origin': 'https://www.forum.ee',
    'Referer': 'https://www.forum.ee/login',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  }

  response = await client.post(
    "https://forum.ee/index.php?app=core&module=ajax&section=register&do=check-email-address",
    headers=headers,
    data={
      "email": email,
      "secure_key": secure_key_value
    }
  )
  
  if response.text == "found":
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
