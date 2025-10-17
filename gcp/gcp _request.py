import requests

url = ' https://python-fg-504-382156928436.europe-west1.run.app '

body = {
    "fasting glucose": 121

}

response = requests.post(url, json=body)

print(response.text)