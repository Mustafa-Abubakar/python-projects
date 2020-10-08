ONE_INCH = 12 # FEET

def main():
    num_feet = int(input("Enter the number of feet: "))
    print("In ",num_feet," Feet there are ",feet_to_inch(num_feet), "inches")


def feet_to_inch(feet):
    return feet * ONE_INCH



main()