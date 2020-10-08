def main():
    outfile = open('test.txt','a')
    outfile.write('Hassan \n')
    outfile.write('Mohammed')
    outfile.close()

    print('appended')

main()