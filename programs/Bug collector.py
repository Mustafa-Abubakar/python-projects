Num_days = 5
total = 0
for day in range(Num_days):
    print("How many Bugs did you collect in day",day+1,"?", end="")
    no_bugs = int(input(" "))
    total += no_bugs
print("The total bugs you collected in during 5 days is ", total, "bugs.")
