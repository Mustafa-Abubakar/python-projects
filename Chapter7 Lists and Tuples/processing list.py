def main():
    list = [1, 2, 3, 4, 5]
    total = 0
    for i in list:
        total += i
        average = total/len(list)
        
    print('Total is ', total)
    print('Average is ', average)
    
main()
