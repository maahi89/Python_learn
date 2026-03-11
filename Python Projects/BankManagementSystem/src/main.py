from bank import Bank
from auth import authenticate
from utils import validate_password


def account_menu(bank, account):
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                if account.deposit(amount):
                    bank.save_accounts()
            except ValueError:
                print("Invalid amount.")

        elif choice == "2":
            try:
                amount = float(input("Enter amount: "))
                if account.withdraw(amount):
                    bank.save_accounts()
            except ValueError:
                print("Invalid amount.")

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")


def main():
    bank = Bank()

    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            password = input("Set password: ")

            if not validate_password(password):
                continue

            account = bank.create_account(name, password)
            print(f"Account created successfully!")
            print(f"Your Account Number is: {account.account_number}")

        elif choice == "2":
            acc_no = input("Enter account number: ")
            password = input("Enter password: ")

            account = authenticate(bank, acc_no, password)

            if account:
                print(f"Welcome {account.name}!")
                account_menu(bank, account)
            else:
                print("Invalid account number or password.")

        elif choice == "3":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
