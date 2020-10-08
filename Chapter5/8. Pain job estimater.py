SQUARE_FEET_OF_ONE_GALLON = 112
CHARGE_PER_LOBOR = 35

def main():
    feet = float(input("Enter the square of feet of wall space to painted: "))
    price_per_gallon = float(input("Enter the price of the paint per gallon: "))
    gallons = num_of_gallons(feet)
    hour = num_of_hours(feet)
    paint_cost = cost_of_paint(gallons,price_per_gallon)
    charge_of_labor = labor_charges(hour)
    total = total_cost(charge_of_labor,paint_cost)
    print("The Number of gallons of paint required are ", gallons, "gallons")
    print("The hours of the labor required are ", hour, "hours")
    print("The cost of the paint is $", paint_cost)
    print("The labor charges is $", charge_of_labor)
    print("The total cost of the paint job is $",total)

    
def num_of_gallons(square_feet):
    gollons = square_feet / SQUARE_FEET_OF_ONE_GALLON
    return gollons


def num_of_hours(square_feet):
    hours = square_feet / 14
    return hours

def cost_of_paint(gallon,price_per_gallon):
    cost = gallon * price_per_gallon
    return cost

def labor_charges(hour):
    charges = hour * CHARGE_PER_LOBOR
    return charges


def total_cost(labor_cost,paint_cost):
    return labor_cost + paint_cost



main()