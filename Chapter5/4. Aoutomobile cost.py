def main():
    loan_payment = float(input("Enter the the monthly cost for loan payment: "))
    insurance = float(input("Enter the monthly cost for insurance payment: "))
    gas =  float(input("Enter the loan cost for gas payment: "))
    oil = float(input("Enter the monthly cos for oil payment: "))
    tire = float(input("Enter the montly cost for tires payment: "))
    maintanance = float(input("Enter the monthly cos for maintanance payment: "))
    monthly_payment= monthly_cost(loan_payment,insurance,gas,oil,tire,maintanance)
    yearly_payment = yearly_cost(monthly_payment)
    print("Your total montly payment is $",monthly_payment,"and your total annual payment is $", yearly_payment)




def monthly_cost(loan,insurance,gas,oil,tires,maintanance):
    total_cost = loan + insurance + gas + oil + tires + maintanance
    return total_cost


def yearly_cost(monthly_cost):
    total_cost = monthly_cost * 12
    return total_cost


main()
