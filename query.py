import json
import httpx

URL = "http://127.0.0.1:8000/iss-stream"


def main():
    with httpx.stream("GET", URL, timeout=None) as response:
        response.raise_for_status()
        print(f"connected: {response.status_code}")

        for line in response.iter_lines():
            if not line or not line.startswith("data:"):
                continue

            payload = json.loads(line.removeprefix("data:").strip())
            print(payload)


if __name__ == "__main__":
    main()
