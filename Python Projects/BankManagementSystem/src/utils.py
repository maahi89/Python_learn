import random

def generate_account_number(existing_accounts):
    while True:
        acc_no = str(random.randint(1000, 9999))
        if acc_no not in existing_accounts:
            return acc_no
        else:   
            print("Account number collision detected. Generating a new one...")

def validate_password(password):
    if len(password) < 4:
        print("Password must be at least 4 characters.")
        return False
    return True
