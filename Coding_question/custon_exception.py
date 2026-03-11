class invalidageerror():
    pass
def vote():
    age=int(input("enter your age: "))
    if age<18:
        raise invalidageerror("you're not eligible to vote")
    print("youre eligible to vote")
try:
    vote()
except invalidageerror as e:
    print(e)