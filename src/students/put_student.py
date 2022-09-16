import requests
from get_token import token

student_id = 2
url = f'http://127.0.0.1:3001/alunos/{student_id}'

headers = {
  'Authorization': token
}

user_data = {
	"nome": "luana",
	"sobrenome": "da silva",
	"email": "laaa@email.com",
	"idade": "20",
	"peso": "60.08",
	"altura": "1.70"
}


response = requests.put(url=url, json=user_data, headers=headers)

if response.ok:
  response_data = response.json()
  print(response_data)

else:
  print(response.status_code)
  print(response.text)
