import requests
from get_token import token

student_id = 3
url = f'http://127.0.0.1:3001/alunos/{student_id}'

headers = {
  'Authorization': token
}

response = requests.delete(url=url, headers=headers)

if response.ok:
  response_data = response.json()
  print(response_data)

else:
  print(response.status_code)
  print(response.text)
