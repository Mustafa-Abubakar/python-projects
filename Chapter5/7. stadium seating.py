def main():
    tickets_sold_in_classA = int(input("How many tickets sold for class A "))
    tickets_sold_in_classB = int(input("How many tickets sold for class B "))
    tickets_sold_in_classC = int(input("How many tickets sold for class C "))

    ClassA_cost = classA_income(tickets_sold_in_classA)
    ClassB_cost = classB_income(tickets_sold_in_classB)
    ClassC_cost = classc_income(tickets_sold_in_classC)

    total_cost = ClassA_cost + ClassB_cost +ClassC_cost

    print("The total cost for all tickets are $", total_cost)



def classA_income(tickets):
    seat_cost = 20
    cost = tickets * seat_cost
    return  cost


def classB_income(tickets):
    seat_cost = 15
    cost = tickets * seat_cost
    return  cost

def classc_income(tickets):
    seat_cost = 10
    cost = tickets * seat_cost
    return  cost


main()



