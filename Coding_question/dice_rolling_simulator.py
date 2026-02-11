import random
while True:
    input("press enter to roll the dice")
    roll= random.randint(1,6)
    print("you rolled: ", roll)
    choice= input("do you want toll again (N to quit)")
    if choice=="n":
        print("thank you for playing")
        break