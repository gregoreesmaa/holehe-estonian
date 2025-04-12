from holehe.core import *
from holehe.localuseragent import *

async def okidoki(email, client, out):
  name = "okidoki"
  domain = "okidoki.ee"
  method = "register"
  frequent_rate_limit = False # Assuming no frequent rate limit based on single HAR

  headers = {
    'User-Agent': random.choice(ua["browsers"]["firefox"]),
    'Accept': 'application/json, */*', # Reflecting server response type and common practice
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest', # Often checked for AJAX endpoints
    'Origin': 'https://www.okidoki.ee',
    'Referer': 'https://www.okidoki.ee/register/',
    'DNT': '1',
    'Connection': 'keep-alive',
  }

  data = {
    "fprt": "register",
    "fullname": "Test User",
    "email": email,
    "passwd1": "TestPassword123!",
    "country": "EE",
    "city": "",
    "city_id": "0",
    "accept": "1",
    "fname": "register"
  }

  exists_flag = False
  rate_limit_flag = False

  response = await client.post(
    'https://www.okidoki.ee/ajax/register/',
    headers=headers,
    data=data
  )

  response_json = response.json()
  validation_errors = response_json.get("validationErrors")
  if any(error.get("name") == "email" for error in validation_errors):
    out.append({
      "name": name,
      "domain": domain,
      "method": method,
      "frequent_rate_limit": frequent_rate_limit,
      "rateLimit": rate_limit_flag,
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
      "rateLimit": rate_limit_flag,
      "exists": False,
      "emailrecovery": None,
      "phoneNumber": None,
      "others": None
    })