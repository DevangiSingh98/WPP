class Password_manager:
    def __init__(self):
        self.passwords = []

    def get_password(self):
        
        if self.passwords:
            return self.passwords[-1]
        return None  

    def set_password(self, newpass):
        
        if newpass not in self.passwords:
            self.passwords.append(newpass) 
            print("Password updated successfully.")
        else:
            print("password has been used before.")

    def is_correct(self, password):
        
        return password == self.get_password()

manager = Password_manager()

while True:
    print("\n1. Set a new password")
    print("2. Check current password")
    print("3. Verify a password")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        newpass = input("Enter a new password: ")
        manager.set_password(newpass)

    elif choice == "2":
        current = manager.get_password()
        if current:
            print("Your current password is:", current)
        else:
            print("No password set yet.")

    elif choice == "3":
        check = input("Enter a password to verify: ")
        if manager.is_correct(check):
            print("Correct password!")
        else:
            print("Incorrect password!")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
