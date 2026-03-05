def add_extra(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

def greet():
    print("Hello")

greet = add_extra(greet)
greet()