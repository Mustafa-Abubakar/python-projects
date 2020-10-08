unit_conversion = 1.60934
print("Miles\t\t\tKilometer")
for miles in range(10,81,10):
    Kilometer = miles * unit_conversion
    print(miles,"\t\t\t\t", format(Kilometer, '.2f'))