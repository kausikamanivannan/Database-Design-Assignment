'''
    Website: https://www.w3schools.com/python/python_classes.asp
    This website helped me form classes and functions. The set up is similar to java except it has different syntax.
    Something I learned from this website is the self key word. "The self keyword is used within these methods to access and modify the instance variables of the object."
'''

class BankAccount:
    def __init__(self, account_name: str, starting_balance: float):
        self.account_name = account_name
        self.balance = starting_balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount

    def get_balance(self):
        return "{self.account_name} has a balance of {self.balance}"

