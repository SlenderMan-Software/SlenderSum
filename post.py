import requests
import json


test_text = """The M134 Minigun is an American 7.62×51mm NATO six-barrel rotary machine gun with a high rate of fire (2,000 to 6,000 rounds per minute).[2] It features a Gatling-style rotating barrel assembly with an external power source, normally an electric motor. The "Mini" in the name is in comparison to larger-caliber designs that use a rotary barrel design, such as General Electric's earlier 20 mm M61 Vulcan, and "gun" for the use of rifle ammunition as opposed to autocannon shells.

"Minigun" refers to a specific model of weapon that General Electric originally produced, but the term "minigun" has popularly come to refer to any externally powered rotary gun of rifle caliber. The term is sometimes used loosely to refer to guns of similar rates of fire and configuration, regardless of power source and caliber."""

base_url = "http://127.0.0.1:5000" 
path = "/new"
url = base_url + path

data = { "text": test_text, "doc_id": "892", "user_id": "steve", "notebook_id": "123" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    print("Request successful!")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)