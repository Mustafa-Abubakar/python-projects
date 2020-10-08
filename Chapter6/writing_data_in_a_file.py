def main():
    # Get the number of subjects
    num_subs = int(input('How many subjects you want to store'))
    # open the fle for writing
    sub_file = open('marks', 'w')
    # get the marks and write into a file
    for count in range(1, num_subs+1):
        sub = float(input('Enter the marks for the subject # ' + str(count) + ": "))
        # write the marks to the file
        sub_file.write(str(sub) + '\n')
    # close the file
    sub_file.close()
    print("Marks saved")


main()
