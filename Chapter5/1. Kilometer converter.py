UNIT_CONVERSION = 0.6214


def main():
    kilometer = float(input("Enter your distance in kilometer: "))
    converter(kilometer)


def converter(kilometer):
    miles = kilometer * UNIT_CONVERSION
    print(kilometer, "Kilometres = ", format(miles, ".3f"), "miles")


main()
