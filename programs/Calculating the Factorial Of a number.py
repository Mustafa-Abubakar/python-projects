Number = int(input("Enter a nonnegative number: "))
while Number < 0:
    print("ERROR!, the number must be positive ", end='')
    Number = int(input())
Factorial = 1
while Number > 0:
    Factorial *= Number
    Number -= 1
print(Factorial)



