import requests

endpoint = "http://localhost:8000/customer-information/1/update/"

data = {
    "name": "Đặng Đức Long Quân",
    "dob": "2000-05-12",
    "socialID": "B18DCCN491",
    "creditScore": 12052000
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
