import json
import os
from account import Account
from utils import generate_account_number

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/accounts.json")


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_accounts()

    def load_accounts(self):
        if not os.path.exists(DATA_FILE):
            return

        with open(DATA_FILE, "r") as file:
            try:
                data = json.load(file)
                for acc_no, details in data.items():
                    self.accounts[acc_no] = Account(
                        acc_no,
                        details["name"],
                        details["password"],
                        details["balance"]
                    )
            except json.JSONDecodeError:
                pass

    def save_accounts(self):
        data = {acc_no: acc.to_dict() for acc_no, acc in self.accounts.items()}
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    def create_account(self, name, password):
        account_number = generate_account_number(self.accounts)
        account = Account(account_number, name, password)
        self.accounts[account_number] = account
        self.save_accounts()
        return account

    def get_account(self, account_number):
        return self.accounts.get(account_number)
