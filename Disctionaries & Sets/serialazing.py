import pickle

filename = 'binary'
name = {
    'Name': 'Mustafa',
    'Age' : 20,
    'Grade' : 'BC Degree'
}
with open(filename, 'wb') as bin:
    pickle.dump(name, bin)
