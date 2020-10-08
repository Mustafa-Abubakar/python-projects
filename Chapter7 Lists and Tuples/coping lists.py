def main():
    list1 = [90, 12, 67, 98, 321, 773, 654, 8, 908, 784, 213, 790, 65, 43, 342, 897]
    print('list1: ', list1)
    list2 = []
    # first way using for loop
    for i in list1:
        list2.append(i)
    print('list2: ',list2)
    list2[-1]=100
    print(list2)
    
    # second way using concatination
    list3 = [] + list1
    print('list3: ', list3)
    


main()
