def main():
    # Initialise the accumulator
    total = 0
    try:
        # Open the file
        infile = open('marks.txt', 'r')

        # Read the marks from the file and add them
        for line in infile:
            marks = int(line)
            total += marks

        # Close the file
        infile.close()

        # Display the total marks
        print('Total marks:', total)
    except Exception as err:
        print(err)


main()
