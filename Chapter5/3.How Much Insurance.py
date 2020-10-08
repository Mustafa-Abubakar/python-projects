MINIMUM_AMOUNT_OF_INSURANCE = 0.8 # AMOUNT OF INSURANCE IN PERCENTAGE

def main():
    replacement_cost = float(input("Enter the the replacement cost of the building: "))
    amount_of_insurance(replacement_cost)


def amount_of_insurance(replacement_cost):
    insurance = replacement_cost * MINIMUM_AMOUNT_OF_INSURANCE
    print("The minimum amount of insurance that you should buy the property is ", format(insurance, ".2f"))


main()