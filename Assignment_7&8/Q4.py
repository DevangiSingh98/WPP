class BankAccount:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    
    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_number, name, initial_deposit=0.0):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, name, initial_deposit)
            print(f"Account created for {name} with balance {initial_deposit}")
    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
        else:
            print("Account not found.")
    
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
        else:
            print("Account not found.")
    
    def check_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_balance()
        else:
            print("Account not found.")
            return None

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __add__(self, other):
        return Employee(self.name + " & " + other.name, self.salary + other.salary)
    
    def __sub__(self, other):
        return self.salary - other.salary
    
    def __str__(self):
        return f"Employee({self.name}, {self.salary})"

# Example usage
bank = Bank()
bank.create_account(101, "Alice", 500)
bank.deposit(101, 200)
bank.withdraw(101, 100)
print("Balance:", bank.check_balance(101))

emp1 = Employee("Alice", 5000)
emp2 = Employee("Bob", 7000)
emp3 = emp1 + emp2
print(emp3)
print("Salary difference:", emp2 - emp1)
