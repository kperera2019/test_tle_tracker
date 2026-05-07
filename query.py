import json
import time
import requests

URL = "http://127.0.0.1:5000/query"

def get_iss_position():
    response = requests.get(URL,timeout=10)
    response.raise_for_status()
    return response.json()

def main():
    while True:
        position = get_iss_position()
        print(position)
        time.sleep(10)


if __name__ == "__main__":
    main()