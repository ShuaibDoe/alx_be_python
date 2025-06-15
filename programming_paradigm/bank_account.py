class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

        def deposit(self, amount):
            if amount <= 0:
                return False
                self.account_balance += amount
                return True
            
        def withdraw(self, amount):
            if amount > 0 and amount <= self.account_balance:
                self.account_balance -= amount
                return f"Withdrawal: ${amount:.2f}"
            elif amount > self.account_balance:
                return "Insufficient funds."
            else:
                return "Withdrawal must be positive."
            
        def display_balance(self):
            return f"Current Balance: ${self.account_balance:.2f}"
            

        
