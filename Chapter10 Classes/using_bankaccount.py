# Test.py file
import bankaccount


def main():
    # Get the starting balance
    start_bal = float(input('Enter the starting balance: '))
    # Create BankAccount Object
    ac = bankaccount.BankAccount(start_bal)
    # Display the initial balance
    print('Initial balance:', ac.get_balance())
    ac.deposit(400)
    print('Balance after deposit:', ac.get_balance())
    ac.withdraw(200)
    print('Balance after withdrawal:', ac.get_balance())
    ac.withdraw(900)


main()

