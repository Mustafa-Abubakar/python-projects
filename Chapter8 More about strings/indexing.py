def main():
    name = 'Mohamed'
    print('indexng in for loop')
    for index in range(len(name)):
        print(name[index])

    #using while loop
    print('indexing in while loop')
    index = 0
    while index < 7:
        print(name[index])
        index += 1

main()