def main():
    num=int(input("Enter the number: "))
    if is_even(num):
        print("Even")
    else:
        print("Odd")


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


main()
