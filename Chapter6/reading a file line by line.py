def main():
    infile = open('test.txt','r')
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    infile.close()

    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    print(line1)
    print(line2)
    print(line3)


main()