import random

def main():
    for i in range(5):
        print("Question ",i+1)
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        print()
        print(num1 , "+", num2, "= ____")
        print()



main()