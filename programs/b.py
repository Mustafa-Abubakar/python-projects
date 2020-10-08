pp = int(input("Enter no of packes "))
am = 99
tam = pp * am
if 10 <= pp <= 19:
    dic = 0.1
    discn = tam * dic
    tamp = tam - discn
    print("you get a discount of 10%")
    print("your tital amount is",tamp )
if 20 <= pp <= 49:
    dic = 0.2
    discn = tam * dic
    tamp = tam - discn
    print("you get a discount of 20%")
    print("your tital amount is", tamp)
if 50 <= pp <= 99:
    dic = 0.3
    discn = tam * dic
    tamp = tam - discn
    print("you get a discount of 30%")
    print("your tital amount is", tamp)
if pp >= 100:
        dic = 0.
        discn = tam * dic
        tamp = tam - discn
        print("you get a discount of 40%")
        print("your total amount is", tamp)

