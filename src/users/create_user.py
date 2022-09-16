import requests


url = 'http://127.0.0.1:3001/users'

user_data = {
  'nome': 'gabriel2',
  'password': 'senha valida',
  'email': 'mail2@gmail.com'
}

response = requests.post(url=url, json=user_data)

if response.ok:
  response_data = response.json()
  print(response_data)

else:
  print(response.status_code)
  print(response.text)
