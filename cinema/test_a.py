refresh_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MTAyNzI0NiwiaWF0IjoxNzUwOTQwODQ2LCJqdGkiOiJkMDZmMDVkNzllY2I0YzBhOTA3ZDM5ZThlODMxODViNyIsInVzZXJfaWQiOjZ9.PC_B5QMxdep05ifL3yCcPd2lMOfk2LYc45uECT66snw"
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUwOTQxMTQ2LCJpYXQiOjE3NTA5NDA4NDYsImp0aSI6ImNhNDUzMDFlNjdiYzQ0ZDFhODk2NDNiYWFhMTVjNTU5IiwidXNlcl9pZCI6Nn0.kCFerqQgQ2sc5o4CCm00hl6dzsLRG1Hfznxfez7PjOk"


import requests

# Replace with your API URL and your JWT access token
API_URL = "http://localhost:8000/spectator/movie_review/create/"

# Sample data to send in the POST request
data =  {
        "id": 2,
        "user": 6,
        "movie": 141,
        "note": 5
    }

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

response = requests.post(API_URL, json=data, headers=headers)

print(f"Status Code: {response.status_code}")
print("Response JSON:", response.json())