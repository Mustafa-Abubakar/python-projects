def main():
    # Get the name of a file
    filename = input('Enter a file name: ')

    # Open the file
    infile = open(filename, 'r')

    # Read the contents of the file and display
    contents = infile.read()
    print(contents)

    # Close the file
    infile.close()


main()
