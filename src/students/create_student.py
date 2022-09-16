import requests
from get_token import token

url = 'http://127.0.0.1:3001/alunos'

headers = {
  'Authorization': token
}

user_data = {
	"nome": "deletado",
	"sobrenome": "Sobrenome",
	"email": "auaiauai@email.com",
	"idade": "50",
	"peso": "80.04",
	"altura": "1.90"
}

response = requests.post(url=url, json=user_data, headers=headers)

if response.ok:
  response_data = response.json()
  print(response_data)

else:
  print(response.status_code)
  print(response.text)
