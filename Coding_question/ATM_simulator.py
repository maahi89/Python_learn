balance=10000
def check_balance():
    print(f"your balance is {balance}")
def deposit():
    global balance
    amount=float(input("Enter the amount to deposit: "))
    if amount<0:
        print("invalid amount")
    else:
        balance += amount
        print(f"amount of {amount} deposited successfully")

def withdraw():
    global balance
    amount=float(input("Enter the amount to withdraw: "))
    if amount<0:
        print("Invalid amount")  
    elif amount>balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print(f"amount of {amount} withdrawn successfully")
while True:
    print("\nHello welcome to the ATM simulator")
    print("1. Check balance")
    print("2. Deposit money")        
    print("3. Withdraw money")
    print("4. Exit")

    choice=input("Enter your choice 1/2/3/4: ")
    if choice=='1':
        check_balance()
    elif choice=='2':
        deposit()
    elif choice=='3':
        withdraw()          
    elif choice=='4':
        print("Thank you for using the ATM simulator. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")  


