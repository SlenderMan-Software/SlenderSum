import requests
import json

# Define the base URL of the server
base_url = "http://127.0.0.1:5000" 

# Define the endpoint path for the summary service
path = "/sum"

# Combine the base URL and path to form the full URL
url = base_url + path

# Prepare the data payload to send in the POST request
# Note: 'summaries' should be defined elsewhere in the code
data = { "summaries": summaries}

# Set the headers to specify the content type as JSON
headers = {"Content-Type": "application/json"}

# Send a POST request to the server with the data and headers
response = requests.post(url, data=json.dumps(data), headers=headers)

# Check the response status code to determine if the request was successful
if response.status_code == 200:
    print("Request successful!")  # Print success message
    print(response.json())        # Print the JSON response from the server
else:
    # Print an error message with the status code and response text
    print(f"Error: {response.status_code}")
    print(response.text)