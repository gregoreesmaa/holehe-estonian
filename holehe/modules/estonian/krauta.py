from holehe.core import *
from holehe.localuseragent import *

# TRUE

async def krauta(email, client, out):
  name = "krauta"
  domain = "k-rauta.ee"
  method = "login"
  frequent_rate_limit = False

  headers = {
    'User-Agent': random.choice(ua["browsers"]["firefox"]),
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.k-rauta.ee',
    'Referer': 'https://www.k-rauta.ee/users/sign_in',
  }

  data = {
    'user[has_physical_card]': '0',
    'user[physical_card_number]': '',
    'user[registration_method]': 'email',
    'user[first_name]': 'Rebase',
    'user[last_name]': 'Onu',
    'user[email]': email,
    'user[password]': 'q1w2e3r4t5y6',
    'user[password_confirmation]': 'q1w2e3r4t5y5',
    'user[marketing_consent_1]': '',
    'user[marketing_consent_2]': '',
    'commit': 'Registreeru',
  }

  response = await client.post(
    "https://www.k-rauta.ee/users",
    headers=headers,
    data=data
  )
  if 'See e-posti aadress on juba kasutusel' in response.text:
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
