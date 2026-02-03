import math
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "0 cannot be divided "
    return a/b

print("simple calculator")
print("Choose otions")
print("1. addition")
print("2. Subtraction")
print("3. multiplication")
print("4. divison")
choice=int(input("enter your choice 1/2/3/4: "))
a=int(input("Enter a number a= "))
b=int(input("Enter a number b= "))
if choice==1:
    print("result: ", a+b)
elif choice==2:
    print("result: ", a-b)
elif choice==3:
    print("result: ", a*b)
elif choice==4:
    print("result: ", a/b)
else:
    print("invalid Choice")   
