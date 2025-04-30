class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")

# Example usage
account = BankAccount("12345678", 500.0)
account.display()
account.deposit(200)
account.withdraw(100)
account.display()
