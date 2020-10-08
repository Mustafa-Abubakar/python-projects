def main():
    # finding items in al ist
    std_id = ['C119681', 'C119616', 'C119651']
    # appending iten in the list
    std_id.append('C119690')
    print('appended C119690', std_id)
    # index
    index = std_id.index('C119681')
    print('index of C119681 is ', index)
    # inserting an item in the list
    std_id.insert(0, 'C119600')
    print('Inserted C119600 in index 0', std_id)
    # Sorting the list
    std_id.sort()
    print('Sorted the list ', std_id)
    # Removing elements in a list
    std_id.remove('C119600')
    print('Removed C119600 from the list', std_id)
    # reversing elements of a list
    std_id.reverse()
    print('Reversed lis: ', std_id)
    del std_id[-1]
    print('You deleted C119651 ', std_id)
    
    num = [90, 12, 67, 98, 321, 773, 654, 8, 908, 784, 213, 790, 65, 43, 342, 897]
    print('The maximum number of the list is ', max(num))
    print('The mimimum number of the list is ', min(num))
    num.sort()
    print(num)


main()