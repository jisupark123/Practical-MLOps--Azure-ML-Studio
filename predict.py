import requests
import json

url = "http://localhost:3000/predict"

data = ["I not love this product"]

input_data = json.dumps(data)
headers = {"Content-Type": "application/json"}
resposne = requests.post(url, input_data, headers=headers)
print(resposne.text)
