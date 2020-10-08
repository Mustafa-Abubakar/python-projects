import pickle
filename = 'binary'
with open(filename, 'rb') as bin:
    name = pickle.load(bin)
print('name: ',name)