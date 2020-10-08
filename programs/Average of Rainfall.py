Month = 12
Montly_rainfall = []
Year = int(input("How many years do you want: "))
print(Year)
for time in range(1,Year+1):
    for month in range(1,13):
        print("Enter the total inches of rain for month", month, end='')
        rain = float(input(":"))
        Montly_rainfall.append(rain)
    total_month = Year + Month
    print("Total month" + str(total_month))