def main():
    # Get the number of subjects
    num_subs = int(input('How many subjects you want to store? '))
    # Open file for writing
    subs_file = open('marks.txt', 'w')
    # Get the marks and write to the file
    for count in range(1, num_subs + 1):
        sub = float(input('Enter the marks for subject # '+ str(count) + ': '))
        # Write the marks to the file
        subs_file.write(str(sub) + '\n')
    # Close the file
    subs_file.close()
    print('Marks saved.')


main()
