import json
import time
import requests
URL = "http://127.0.0.1:5000/query"


def main():
    while True:
        with requests.get(URL,stream=True) as response:
            response.raise_for_status()
            print(f"connected: {response.status_code}")
            for line in response.iter_lines():
                if not line:
                    continue

                payload = json.loads(line.strip())
                print(payload)
                time.sleep(3)


if __name__ == "__main__":
    main()
