def main():
    try:
        # Get hours worked, hourly pay rate
        hours = int(input('Enter hours worked: '))
        rate = float(input('Enter hourly pay rate: '))

        # calculate the gross pay and display
        gross_pay = hours * rate
        print('Gross pay: $', gross_pay, sep='')
    except ValueError as err:
        print(err)


main()
