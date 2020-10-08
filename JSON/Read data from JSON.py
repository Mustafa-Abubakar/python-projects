import json
file_name = 'numbers.json'
with open(file_name) as infile:
    numbers = json.load(infile)
    
print(numbers)
for i in numbers:
    if i.startswith('3') or i.endswith('3'):
        print('found')