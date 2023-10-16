import requests

url = "http://localhost:8080/upload"

payload = {}
files=[
  ('file',('nhucc.png',open('D:/Job_KHTN/Web_img/nhucc.png','rb'),'image/png'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)