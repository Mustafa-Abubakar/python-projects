setA = set([12,33,44,69,66,80,92,5,96,122,187])
setB = set([12,66,80,5,92,99])

# set union
print('Union of sets')
union1 = setA | setB
union2 = setA.union(setB)
print(union1)
print(union2)
print()

# intersection of the sets
print('intresection of sets')
intr1 = setA.intersection(setB)
intr2 = setA & setB
print(intr1)
print(intr2)
print()

#difference of two sets
print('difference of sets')
diff1 = setA.difference(setB)
diff2 = setA - setB
print(diff1)
print(diff2)
print()

#symmetric diffeence
print('Symetric difference  of sets')
sdiff1 = setA.symmetric_difference(setB)
sdiff2 = setA ^ setB
print(sdiff1)
print(sdiff2)
print()