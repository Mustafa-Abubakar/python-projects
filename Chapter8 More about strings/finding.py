def main():
    string = 'He is ten years old.'
    position = string.find('ten')
    if position != -1:
        print('ten is found at position', position)
    else:
        print('ten is not found')


main()
