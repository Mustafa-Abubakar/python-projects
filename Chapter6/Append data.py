def main():
    # step1: open the file
    outfile = open('name.txt', 'a')
    # step2: processing the file
    outfile.write('Jamhuriya university of science and technology.\n')
    outfile.write('JUST.')
    # step3: close the file
    outfile.close()


main()
