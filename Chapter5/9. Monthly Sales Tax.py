COUNTRY_TAX = 0.025
STATE_TAX = 0.05

def main():
    month_sales = float(input("Enter the total sales of the month: "))
    Country_Tax = country_tax(month_sales)
    State_Tax = state_tax(month_sales)
    total = total_tax(Country_Tax,State_Tax)
    print("The amount of country tax is $",Country_Tax)
    print("The amount of state tax is $",State_Tax)
    print("Te total sales tax is $",total)



def country_tax(month_sales):
    tax = month_sales * COUNTRY_TAX
    return tax


def state_tax(month_sales):
    tax = month_sales * STATE_TAX
    return tax


def total_tax(country,state):
    total = country + state
    return total


main()
