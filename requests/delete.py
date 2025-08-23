import requests
import json

# Base URL of the server
base_url = "http://127.0.0.1:5000" 

# API endpoint for the delete operation
path = "/delete"

# Construct the full URL for the request
url = base_url + path

# Data to be sent in the request body
data = { "doc_id": "892" }

# Headers specifying the content type of the request
headers = {"Content-Type": "application/json"}

# Send a POST request to the server with the data and headers
response = requests.post(url, data=json.dumps(data), headers=headers)

# Check the response status code to determine success or failure
if response.status_code == 200:
    # If the request was successful, print the response
    print("Request successful!")
    print(response.json())
else:
    # If the request failed, print the error code and response text
    print(f"Error: {response.status_code}")
    print(response.text)