# coin.py file
import random


class Coin:
    def __init__(self):
        self.__sideup = 'Heads'
        # self.sideup = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup

