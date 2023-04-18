from BankAccount import BankAccount

account = BankAccount("Kausika's Checking Account", 7000)

account.deposit(500)
print(account.get_balance())

account.withdraw(1100)
print(account.get_balance())