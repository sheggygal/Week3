class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit of", amount, "completed.")
        self.print_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            decision = input("Withdrawal amount exceeds available balance. Do you want to cancel the transaction? (yes/no): ")
            if decision.lower() == 'yes':
                print("Transaction canceled.")
            elif decision.lower() == 'no':
                self.balance = 0
                print("Withdrawal of", self.balance, "completed.")
                self.print_balance()
            else:
                print("Invalid input. Transaction canceled.")
        else:
            self.balance -= amount
            print("Withdrawal of", amount, "completed.")
            self.print_balance()

    def transfer(self, recipient, amount):
        if amount > self.balance:
            print("Transfer amount exceeds available balance. Transfer canceled.")
        else:
            self.balance -= amount
            recipient.deposit(amount)
            print("Transfer of", amount, "to", recipient.owner, "completed.")
            self.print_balance()

    def get_balance(self):
        return self.balance

    def print_balance(self):
        print("Current Balance:", self.balance)


alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob", 500)

alice_account.deposit(500)

alice_account.withdraw(2000)

alice_account.transfer(bob_account, 200)

print("Final Balance for", alice_account.owner + ":", alice_account.get_balance())
print("Final Balance for", bob_account.owner + ":", bob_account.get_balance())


