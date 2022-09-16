import requests

url = 'http://127.0.0.1:3001/alunos'

response = requests.get(url=url)

if response.ok:
  response_data = response.json()
  print(response_data)

else:
  print(response.status_code)
  print(response.text)
