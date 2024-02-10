import requests

# Set up the request headers
url = 'https://reqres.in/api/register'

# Define the request body
body = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

# Send the request
response = requests.post(url, json=body)

# Verify the response status code
assert response.status_code == 200

# Parse the response JSON
result = response.json()
print(result)

# Extract the token from the response
message = result['token']

# Assert that the token matches the expected value
assert message == "QpwL5tke4Pnpja7X4"