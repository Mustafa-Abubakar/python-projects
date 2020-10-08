price = {}
discounts = dict()

for i in range(5):
    price['Books'] = 12
    price['Pens'] = 8
    price['Dictionaries'] = 45
    price['Mobiles'] = 120
    price['Computers'] = 420
    discounts['Books'] = 0.1
    discounts['Pens'] = 0.07
    discounts['Dictionaries'] = 0.5
    discounts['Mobiles'] = 2
    discounts['Computers'] = 12
print(price)
print(discounts)
print()
print(price.get('Books','Sorry you do not have any book'))
print(discounts.items())
print(price.keys())
print(price.values())
print(discounts.pop('Books', 'not found'))
print(discounts)
print(price.popitem())
print(price)