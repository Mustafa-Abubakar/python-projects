import json

number = ['1', '5', '6', '7', '9', '11', '13']
file_name = 'numbers.json'
with open(file_name, 'w') as outfile:
    json.dump(number, outfile)
