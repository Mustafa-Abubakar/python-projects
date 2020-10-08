import json
filename = 'userdata.json'
firs_name = input('First Name: ')
last_name = input('Last Name: ')
Age = int(input('Age: '))

with open(filename, 'w') as user:
    json.dump(firs_name, user)

print('We saved your data')