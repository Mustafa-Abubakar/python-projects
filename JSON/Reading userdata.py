import json
filename = 'userdata.json'
with open(filename) as user:
    users = json.load(user)

print(users)