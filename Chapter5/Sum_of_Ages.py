def main():
    #Get tje user's age
    first_age = int(input("Enter your age: "))
    #Get the user's best friend's age
    second_age = int(input("Enter your best friend's Age: "))
    #Get the total of ages
    total = sum(first_age,second_age)
    print("Together you're ", total,"ages old")


def sum(num1,num2):
    result = num1 + num2
    return result


main()