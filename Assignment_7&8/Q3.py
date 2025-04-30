class BankAccount:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposits money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        """Withdraws money from the account if sufficient funds exist."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ${amount:.2f}. New balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            print("Invalid withdrawal amount!")

    def display_balance(self):
        """Displays the current balance."""
        print(f"Account {self.account_number} - {self.name}: Balance = ${self.balance:.2f}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        """Creates a new bank account."""
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            print("Account number already exists!")
            return
        name = input("Enter account holder's name: ")
        initial_deposit = float(input("Enter initial deposit amount: "))
        self.accounts[account_number] = BankAccount(account_number, name, initial_deposit)
        print("Account created successfully!")

    def deposit_money(self):
        """Deposits money into an existing account."""
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            amount = float(input("Enter deposit amount: "))
            self.accounts[account_number].deposit(amount)
        else:
            print("Account not found!")

    def withdraw_money(self):
        """Withdraws money from an existing account."""
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            amount = float(input("Enter withdrawal amount: "))
            self.accounts[account_number].withdraw(amount)
        else:
            print("Account not found!")

    def check_balance(self):
        """Displays the balance of an existing account."""
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            self.accounts[account_number].display_balance()
        else:
            print("Account not found!")

# Interactive Menu
bank = Bank()

while True:
    print("\n--- Bank System ---")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        bank.create_account()
    elif choice == "2":
        bank.deposit_money()
    elif choice == "3":
        bank.withdraw_money()
    elif choice == "4":
        bank.check_balance()
    elif choice == "5":
        print("Exiting the bank system. Thank you!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
