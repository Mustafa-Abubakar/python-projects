DISCOUNT_PERCENTAGE = 0.2

def main():
    reg_price = get_regular_price()
    sale_price = reg_price - discount(reg_price)
    print("Item's original price is : $", reg_price)
    print("20% of discount $", discount(reg_price))
    print("Your sale price is: $", sale_price)

def get_regular_price():
    price = int(input("Enter The regular price: "))
    return price


def discount(price):
    discount = DISCOUNT_PERCENTAGE * price
    return discount

main()