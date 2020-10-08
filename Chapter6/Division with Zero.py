def main():
    # Get 2 numbers
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

    # Divide the 2 numbers and display the result
    if num2 != 0:
        result = num1 / num2
        print(num1, 'divided by', num2, '=', result)
    else:
        print('Cannot divide by zero')


main()
