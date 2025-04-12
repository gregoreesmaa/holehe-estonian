from holehe.core import *
from holehe.localuseragent import *

# OK

async def naminami(email, client, out):
  name = "naminami"
  domain = "nami-nami.ee"
  method = "register"
  frequent_rate_limit = False

  boundary = '----HoleheBoundary2gfx2d4'

  headers = {
    'User-Agent': random.choice(ua["browsers"]["firefox"]),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Origin': 'https://nami-nami.ee',
    'Referer': 'https://nami-nami.ee/registreeru',
    'Content-Type': f'multipart/form-data; boundary={boundary}'
  }

  multipart_body = (
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"_method\"\r\n\r\n"
    f"POST\r\n"
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"users[id]\"\r\n\r\n"
    f"\r\n"
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"data[User][name]\"\r\n\r\n"
    f"Test\r\n" 
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"data[User][last_name]\"\r\n\r\n"
    f"User\r\n" 
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"data[User][username]\"\r\n\r\n"
    f"testuser{str(random.randint(10000, 99999))}\r\n" 
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"data[User][email]\"\r\n\r\n"
    f"{email}\r\n" 
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"data[User][telephone]\"\r\n\r\n"
    f"\r\n" 
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"data[User][password]\"\r\n\r\n"
    f"\r\n" 
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"image\"; filename=\"\"\r\n" 
    f"Content-Type: application/octet-stream\r\n\r\n"
    f"\r\n"
    f"--{boundary}--\r\n"
  )

  response = await client.post(
    'https://nami-nami.ee/registreeru',
    headers=headers,
    data=multipart_body.encode('utf-8')
  )
  if "Selle aadressiga kasutaja on juba loodud" in response.text:
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
