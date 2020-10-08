Number_of_subjects = int(input("Geli inta maadoo ee aad qaadaneyso?"))
Total = 0.0
i = 1
while i <= Number_of_subjects:
    print("Geli magaca maadada", i, "-aad", end="")
    Subject_name = input("")
    i = i+1
    for sub in range(1):
        print("Geli natiijadeeda: ", end="")
        Marks = float(input(""))
        print(Subject_name, ":", Marks)
        Total += Marks
Average = Total / Number_of_subjects
print("Your Total marks is: ", Total)
print("Your average is :", Average)
