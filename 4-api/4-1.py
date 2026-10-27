import requests

uri = "https://portal.app.cent-su.org/api/funnyname/random?n=5"
response = requests.get(uri)

##deseralize the response to python obj
#data = response.json() #parses for you
#print(data)
#print(type(data))

#deserialize response to python obj
response.raise_for_status() #throw an exception if the request failed
data = response.json() #parses for you
for name in data:
    print(name['first'], name['last'])




import os

import requests

url = "https://portal.app.cent-su.org/api/weather/geocode"
params = {
    "language": "en",
    "count": 2,
    "place": "Syracuse, New York",
}
headers = {
    "accept": "application/json",
    "X-API-KEY": os.environ["CENTSU_API_KEY"],
}

response = requests.get(url, params=params, headers=headers)
response.raise_for_status()
data = response.json()


print(data)