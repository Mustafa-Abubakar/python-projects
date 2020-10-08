Days_works = int(input("Enter the days of work: "))
total = 0
OnePenny = 0.01
print("Day\t\t\tSalary")
for day in range(Days_works):
    pennies_of_the_day = 2 ** day
    Amount_of_the_day = pennies_of_the_day * OnePenny
    print(day+1, "\t\t\t", "$", Amount_of_the_day, sep = '')
    total += Amount_of_the_day
print("\nThe total amount of pay in ", Days_works, " days is: $", format(total, '.2f'), sep = '')
