import random

def main():
    # open the file for reading
    file = open('number', 'w')
    # using loop write rondam numbers to a file
    for count in range(10):
        num = random.randint(0, 20)
        file.write(str(num) + '\n')

    # close the file
    file.close()
    print('numbers saved')

main()

