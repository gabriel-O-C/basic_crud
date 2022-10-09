import requests

url = 'http://127.0.0.1:3001/tokens'

user_data = {
  'password': 'senha valida',
  'email': 'mail2@gmail.com'
}

response = requests.post(url=url, json=user_data)

if response.ok:
  response_data = response.json()
  token = response_data['token']
  with open('.env', 'w') as file:
    file.write(token)
else:
  print(response.status_code)
  print(response.text)
