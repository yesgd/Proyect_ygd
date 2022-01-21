# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample Json
userJSON = '{"first_name":"Jhon", "last_name": "Doe", "age": 30}'

# Parse to dict 
user = json.loads(userJSON)

print (user)
print (user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}
carJSON = json.dumps(car)

print (carJSON)