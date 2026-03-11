def authenticate(bank, account_number, password):
    account = bank.get_account(account_number)
    if account and account.password == password:
        return account
    return None
