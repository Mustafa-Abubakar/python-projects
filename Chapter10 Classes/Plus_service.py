import json


class Service:
    def __init__(self, number):
        self.__number = number
    
    def set_account(self, pin):
        # opening json file
        pin = pin
        user_account = self.__number + ' ' + pin
        with open('accounts.json', 'w') as acc:
            json.dump(user_account, acc)
    
    def account(self):
        with open('accounts.json') as acc:
            accounts = json.load(acc)
        return accounts
