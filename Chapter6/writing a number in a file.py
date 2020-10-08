def main():
    print("Enter three numbers: ")
    num1 = int(input("Enter Number1: "))
    num2 = int(input("Enter Number2: "))
    num3 = int(input("Enter Number3: "))

    outfile = open('number.txt','w')
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    outfile.close()

main()