# test.py file
import Coin


def main():
    # Create an object
    my_coin = Coin.Coin()
    print('This side is up:', my_coin.get_sideup())
    print('Tossing the coin ten times')
    for i in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())


main()
