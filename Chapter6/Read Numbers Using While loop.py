def main():
    #step1: open the file
    file = open('marks.txt','r')
    #step2: process the file
    line  = file.readline()
    while line != ' ':
        num = float(line.rstrip('\n'))
        print(num)
        line = file.readline()
    #step3: close the file
    file.close()
main()