

import requests
import json

url = 'http://localhost:9000/'
params ={'query': 'It was awesome movie'}
response = requests.get(url, params)
print(response.json())

