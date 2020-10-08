def main():
    filename = input('Enter a file name: ')
    if filename.endswith('.txt'):
        print('The file is text file')
    elif filename.endswith('.docx'):
        print('The file is ms word file')
    else:
        print('Unknown file')


main()
