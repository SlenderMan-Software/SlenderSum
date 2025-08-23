import requests
import json

# Sample text to be sent in the POST request
test_text = """The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."""

# Base URL of the server
base_url = "http://127.0.0.1:5000" 
# Endpoint path for the POST request
path = "/new"
# Full URL for the POST request
url = base_url + path

# Data payload to be sent in the POST request
data = { 
    "text": test_text,       # Text content to process
    "doc_id": "892",         # Document ID
    "user_id": "steve",      # User ID
    "notebook_id": "123"     # Notebook ID
}
# Headers specifying the content type as JSON
headers = {"Content-Type": "application/json"}

# Sending a POST request to the server
response = requests.post(url, data=json.dumps(data), headers=headers)

# Checking the response status code
if response.status_code == 200:
    # If the request is successful, print the response
    print("Request successful!")
    print(response.json())
else:
    # If the request fails, print the error code and response text
    print(f"Error: {response.status_code}")
    print(response.text)