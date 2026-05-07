import time
import httpx
URL='http://localhost:8000/iss-stream'
while True:
    response = httpx.get(URL,timeout=10)
    print(response.status_code)
    print(response.json())
    time.sleep(15)