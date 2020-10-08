Ns = int(input("Enter number of seconds: "))
if Ns >= 60 and Ns <= 3600:
    minutes = Ns // 60
    seconds = Ns %60
    print(minutes, "minutes", "and", seconds, "seconds")
elif  Ns >= 3600 and Ns < 86400:
    hours = Ns // 3600
    minutes = (Ns % 3600) // 60
    seconds = Ns % 60
    print(hours,  "hours,", minutes, "minutes", "and", seconds, "seconds")
elif Ns >= 86400:
    day = Ns // 86400
    hours = (Ns // 86400) % 3600
    minutes = ( (Ns % 86400) % 3600) // 60
    seconds = Ns % 60
    print(day , "days" , hours, "hours" , minutes, "minutes", "and", seconds, "seconds")