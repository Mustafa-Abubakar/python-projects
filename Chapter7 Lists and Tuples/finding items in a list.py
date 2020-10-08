def main():
    # finding items in al ist
    std_id = ['C119681', 'C119616', 'C119651']
    search = input('enter student id: ')
    if search in std_id:
        print(search)
    else:
        print('Not found')


main()
