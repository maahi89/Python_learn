class Account:
    def __init__(self, account_number, name, password, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self.balance += amount
        print(f"₹{amount} deposited successfully.")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient balance.")
            return False
        self.balance -= amount
        print(f"₹{amount} withdrawn successfully.")
        return True

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def to_dict(self):
        return {
            "name": self.name,
            "password": self.password,
            "balance": self.balance
        }
