
import requests, json, sys

url = "https://python-fg-504-382156928436.europe-west1.run.app"

def test(input):
    try:
        print(f"\n Input: {input}")
        r = requests.post(url, json=input, timeout=10)
        print(r.status_code, r.json())
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    test({"fasting glucose": 99})  # normal
    test({"fasting glucose": 123}) # prediabetes
    test({"fasting glucose": 131})  # diabetes