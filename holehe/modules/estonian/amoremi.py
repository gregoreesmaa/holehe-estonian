import urllib.parse

from holehe.core import *
from holehe.localuseragent import *

# OK

async def amoremi(email, client, out):
  name = "amoremi"
  domain = "amoremi.ee"
  method = "register"
  frequent_rate_limit = False

  headers = {
    'User-Agent': random.choice(ua["browsers"]["firefox"]),
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.amoremi.ee',
    'Referer': 'https://www.amoremi.ee/register',
  }

  data = {
    'regusername': 'testuser',
    'regpassword': '',
    'email': email,
    'register_submit': '',
  }
  encoded_data = urllib.parse.urlencode(data)

  response = await client.post('https://www.amoremi.ee/register',
                               headers=headers, data=encoded_data)

  if "Kasutaja '" + email + "' aadressiga on juba registreeritud" in response.text:
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
