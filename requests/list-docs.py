import requests
import json

base_url = "http://127.0.0.1:5000" 
path = "/list-docs"
url = base_url + path

data = { "doc_id": "892" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    print("Request successful!")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)