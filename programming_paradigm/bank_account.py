class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

        def deposit(self, amount):
            if amount > 0:
                self.account_balance += amount
                return f"Deposit: ${amount:.2f}"
            else:
                return "Deposit must be positive."
            
        def withdraw(self, amount):
            if amount > 0 and amount <= self.account_balance:
                self.account_balance -= amount
                return f"Withdrawal: ${amount:.2f}"
            elif amount > self.account_balance:
                return "Insufficient funds."
            else:
                return "Withdrawal must be positive."
            
        def display_balance(self):
            return f"Account Balance: ${self.account_balance:.2f}"
            

        
