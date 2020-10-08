print('Welcome to our university')
Request = input("Do you want to join the university: ")
if Request.lower() == "yes":
    Condition = input("Do you graduated to the secondary school: ")
    if Condition.lower() == "yes":
        print("Welcome to the admissiomn part")
        Name = input("Enter your name: ")
        School = input("Enter your graduated school: ")
        Gender = input("Enter your gender: ")
        Age = int(input("Enter your age:  "))
        if Gender.lower() == "male":
            if Age >= 18:
                print("Mr: ", Name , "We eccepted your request.")
            else:
                print("Sorry! we cant eccept you")
        else:
            if Gender.lower() == "female":
                if Age >= 16:
                    print("Ms: ", Name, "We eccepted your request.")
                else:
                    print("Sorry! we cant eccept you")
    else:
        print("Sorry! Go to the secndary school")
else:
    print("Dear customer, this this the admission office, if you need other service go to the next office")


