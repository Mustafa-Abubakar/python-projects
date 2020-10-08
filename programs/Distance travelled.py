speed = int(input("What is the speed of your vehicle in mph ? "))
Time = int(input("How many hours has it travelled? "))
print("Hour\t\tDistance travelled ")
for time in range(1,Time+1):
    Distance = speed * time
    print(time,"\t\t\t",Distance)