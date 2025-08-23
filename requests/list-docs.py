import requests
import json

# Base URL of the API server
base_url = "http://127.0.0.1:5000" 

# API endpoint path for listing documents
path = "/list-docs"

# Construct the full URL for the API request
url = base_url + path

# Data payload to be sent in the POST request
data = { "doc_id": "892" }

# Headers specifying the content type as JSON
headers = {"Content-Type": "application/json"}

# Send a POST request to the API with the data and headers
response = requests.post(url, data=json.dumps(data), headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Request successful!")  # Print success message
    print(response.json())        # Print the JSON response from the server
else:
    # Print error details if the request failed
    print(f"Error: {response.status_code}")
    print(response.text)