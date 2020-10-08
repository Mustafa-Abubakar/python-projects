def main():
    with open('test.txt', 'r+') as infile:
        # step2: process the file
        file_content = infile.read()
        # infile.write('\nMustafa+\nAbubakar+\nAbdullahi')
    
    print(file_content)


main()
