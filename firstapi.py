import requests
import json

url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"

payload = json.dumps({
  "name": "Akshat Saxena",
  "regNo": "0827CS221022",
  "email": "akshatsaxena220177@acropolis.in"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
