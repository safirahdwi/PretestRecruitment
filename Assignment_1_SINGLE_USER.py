import requests
import json

# Define the URL of the request
url = 'https://reqres.in/api/users/2'

# Send the request
response = requests.get(url)

# Verify the status code
assert response.status_code == 200

# Parse the response body
result = response.json()
print(result)

# Get the message from the response
emailuser = result['data']['email']
message = result['support']['text']

# Assert the message
assert emailuser == "janet.weaver@reqres.in"
assert message == "To keep ReqRes free, contributions towards server costs are appreciated!"
