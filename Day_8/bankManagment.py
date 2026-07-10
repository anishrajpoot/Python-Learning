class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")


account = BankAccount("123456789", "Alice", 1000)

account.check_balance()
account.deposit(500)
account.withdraw(300)
account.check_balance()