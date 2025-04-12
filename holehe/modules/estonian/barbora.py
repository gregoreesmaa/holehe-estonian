import random

from holehe.core import *
from holehe.localuseragent import *

# OK

async def barbora(email, client, out):
  name = "barbora"
  domain = "barbora.ee"
  method = "register"
  frequent_rate_limit = False

  headers = {
    'User-Agent': random.choice(ua["browsers"]["firefox"]),
    'Accept': '*/*',
  }

  url = f"https://barbora.ee/api/eshop/v1/user/CheckCustomerAlreadyRegistered?email={email}"

  response = await client.get(url, headers=headers)

  response_text = response.text
  if response_text == "true":
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
