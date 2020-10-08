Run = int(input("How many times did you run around the racetrack? "))
total = 0
time = []
for r in range(1, Run + 1):
    print("Enter the time of lap ", r, ": ", end="")
    Time = int(input(""))
    time.append(Time)
    total += Time
    average = total / r

print("The time of your fastest lap is ", min(time))
print("The time of your slowest lap is ", max(time))
print("The average of your lap time is ", format(average, '.1f'))
