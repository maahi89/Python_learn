email=input("Enter the email: ")
if "@" in email:
    username, domain = email.split("@")
    print(f"username: {username}")
    print(f"domain: {domain}")
else:
    print("Invalid email address")    
