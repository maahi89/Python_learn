while True:
        import random
        import string
        length=input("Enter the length of the password: ")
        password=" "
        characters = string.ascii_letters + string.digits + string.punctuation
        for i in range(int(length)):
            password += random.choice(characters)
        print("generated password is", password)    
