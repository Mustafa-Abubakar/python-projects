import random
def main():
    num1 = random.randint(0, 20)
    num2 = random.randint(0, 20)
    print("What is ",num1,"+",num2, "?")
    result = int(input("Enter the Answer: "))
    if result == num1+num2:
        print("The  Answer is Correct.")
    else:
        print("The Answer is Incorrect.")


main()

