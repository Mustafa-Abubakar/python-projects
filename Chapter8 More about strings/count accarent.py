def main():
    count = 0
    name = input('Enter your name: ')
    for ch in name:
        if ch == 't' or ch == 'T':
            count += 1
    print('The letter T appears', count, 'times')


main()
