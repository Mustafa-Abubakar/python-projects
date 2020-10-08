StartingNumberOfOrganization = int(input("Enter the starting number of the 0rgation: "))
Daily_increase = int(input("Enter the daily increase of the organization: "))
Multiplying_days = int(input("Enter the number of days: "))
Daily_increase /= 100
Population = StartingNumberOfOrganization
print("Day Approximate\t\t\tPopulation")
for day in range(1, Multiplying_days+1):
    print(day, "\t\t\t\t\t\t", format( Population, '.3f'))
    Population += Daily_increase * Population