from holehe.core import *
from holehe.localuseragent import *

async def stena(email, client, out):
  name = "stena"
  domain = "stena.ee"
  method = "register"
  frequent_rate_limit = False

  headers = {
    'User-Agent': random.choice(ua["browsers"]["firefox"]),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.stena.ee',
    'Referer': 'https://www.stena.ee/user/register',
  }

  data = {
    'name': 'holehetester',
    'mail': email,
    'username': '',
    'familyname': 'test',
    'form_id': 'user_register',
    'iam_human_checkbox': '1',
    'iam_human_checkbox1': '1',
    'op': 'Registration'
  }

  response = await client.post(
    "https://www.stena.ee/user/register",
    headers=headers,
    data=data
  )

  if "уже зарегистрирован" in response.text:
    out.append({
      "name": name,
      "domain": domain,
      "method": method,
      "frequent_rate_limit": frequent_rate_limit,
      "rateLimit": False,  # Default assumption
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
      "rateLimit": False,  # Default assumption
      "exists": False,
      "emailrecovery": None,
      "phoneNumber": None,
      "others": None
    })
