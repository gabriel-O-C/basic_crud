token = 'Bearer '

with open('.env', 'r') as file:
  token += file.read()
