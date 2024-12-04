class BankAccount(object):
    balance = 0  # Class attribute for initial balance

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}'s account. Balance: ${self.balance:.2f}"

    def show_balance(self):
        print(f"{self.name}'s account. Balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Error! You cannot deposit 0 or a negative amount.")
            return
        else:
            print(f"{self.name}'s account. Amount the user is depositing: ${amount:.2f}")
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error! You cannot withdraw more than what is currently in your bank account!")
            return
        else:
            print(f"{self.name}'s account. Amount the user is withdrawing: ${amount:.2f}")
            self.balance -= amount
            self.show_balance()


# Testing the class
my_account = BankAccount("Anna")

print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)
