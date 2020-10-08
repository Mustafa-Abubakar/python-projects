Nstudents = int(input("How many students do you have? "))
Ntests = int(input("How many test score each student? "))
for student in range(Nstudents):
    total = 0.0
    print("Student Number", student+ 1)
    print("-" *16)
    for test in range(Ntests):
        print("Test Number", test+1, end="")
        Score = float(input(": "))
        total += Score
        average = total / Ntests
    print("The average of student ",student+1, "is :",format(average, '.2f') )