import requests
import json

summaries = ["The Central Intelligence Agency (CIA) is a civilian foreign intelligence service of the U.S. government responsible for collecting and analyzing intelligence, conducting covert operations, and advancing national security.  Headquartered in Langley, Virginia, it's a key part of the U.S. Intelligence Community, reporting to the Director of National Intelligence.  The CIA's functions include human intelligence (HUMINT) coordination, support for foreign intelligence services, and paramilitary operations.  Its history includes involvement in numerous controversial events, such as coups in Iran, Guatemala, and Chile, and operations like MKUltra and CHAOS.  The agency has faced scrutiny for its use of torture, assassination, and other controversial tactics.", 
'The M134 Minigun is a 7.62 mm six-barrel rotary machine gun with a high rate of fire (2,000-6,000 rounds per minute). It uses a Gatling-style rotating barrel assembly and an external power source, typically an electric motor.  The term "minigun" is often used more broadly to describe similar externally powered rotary guns.', 
"Free France, led by Charles de Gaulle, was a government-in-exile established in London in 1940 after the Fall of France.  It opposed the Vichy French government and fought alongside the Allies against Axis forces, gaining support in several French colonies.  De Gaulle's Appeal of 18 June called for French resistance against Nazi Germany.", 
]


base_url = "http://127.0.0.1:5000" 
path = "/sum"
url = base_url + path

data = { "summaries": summaries}
headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    print("Request successful!")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)