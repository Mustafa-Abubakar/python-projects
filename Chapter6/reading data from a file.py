def main():
    # Open the file for reading
    myfile = open('marks', 'r')
    # Read all the lines in the file
    for line in myfile:
        num = float(line.rstrip('\n'))
        print(num)
    # Close the file
    myfile.close()

main()

