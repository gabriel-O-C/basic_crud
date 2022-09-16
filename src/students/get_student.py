import requests
student_id = 2
url = f'http://127.0.0.1:3001/alunos/{student_id}'
response = requests.get(url=url)

if response.ok:
  response_data = response.json()
  print(response_data)

else:
  print(response.status_code)
  print(response.text)
