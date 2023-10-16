import requests
import os

url = "http://localhost:8080/upload"

payload = {}
files=[
  ('file',('nhucc.png',open('nhucc.png','rb'),'image/png'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)
os.system("del nhucc.png")


print(response.text)