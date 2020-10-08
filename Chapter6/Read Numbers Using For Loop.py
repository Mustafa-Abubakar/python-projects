def main():
    # step1: open the file
    file = open('marks.txt', 'r')
    # step2: processing(read all the lines in files)
    for line in file:
        num = float(line.rstrip('\n'))
        print(num)

    # step3: close the file
    file.close()


main()
