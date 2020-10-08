def main():
    # Writing the names of 3 friends
    print('Enter the names of 3 friends:')
    friend1 = input('Enter friend1: ')
    friend2 = input('Enter friend2: ')
    friend3 = input('Enter friend3: ')

    outfile = open('test.txt', 'a')
    outfile.write(friend1 + '\n')
    outfile.write(friend2 + '\n')
    outfile.write(friend3 + '\n')
    outfile.close()
    print('Saved.')


main()
