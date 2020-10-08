def main():
    total = 0
    try:
        file = open('marks.txt', 'r')
        for line in file:
            amount = int(line)
            total += amount

    except Exception as ex:
        print(ex)
    else:
        print('Total:', total)
    finally:
        file.close()


main()
