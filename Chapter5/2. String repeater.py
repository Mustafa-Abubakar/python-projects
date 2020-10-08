def main():
    Text = input("enter the text: ")
    Number = int(input("Enter the number of times that yo want to repeat: "))
    repeater(Text,Number)


def repeater(text,number):
    print(text* number)


main()