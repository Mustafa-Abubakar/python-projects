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

    # except FileNotFoundError:
    except IOError:
        print('An error occurred trying to read  the file')
    except ValueError:
        print('Non-numeric data found in the file')
    except:
        print('An error occurred')


main()
