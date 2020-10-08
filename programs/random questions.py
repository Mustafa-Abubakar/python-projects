import random

Addition = "+"
Subtraction = "-"
Multiply = "*"
Division = "/"
Result = 0


def main():
    Answer = True
    i = 1
    while Answer:
        number1 = random.randint(-100,100)
        number2 = random.randint(-100, 100)
        operation = random.randint(1,4)
        qusetiom(num1=number1, operation=operation, num2=number2)
        if operation == 1:
            print(i, ".", number1, "+", number2,"=_____")

        elif operation == 2:
            print(i, ".", number1, "-", number2, "=_____")

        elif operation == 3:
            print(i, ".", number1, "*", number2, "=_____")

        elif operation == 2:
            print(i, ".", number1, "/", number2, "=_____")

        Answer=float(input())

        if Answer == Result:
            Answer = True
        else:
            Answer = False
            print("The Right Answer is ", Result)
            print("Your score is: ", (i - 1) * 10)

        i += 1

def qusetiom(num1, operation, num2):
    global Result
    if operation == 1:
        Result = num1 + num2

    elif operation == 2:
        Result = num1 - num2

    elif operation == 3:
        Result = num1 * num2

    elif operation == 4:
        Result = num1 / num2


main()

