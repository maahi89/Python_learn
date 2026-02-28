# def add(a, b):
#     return a + b

# # define values for the parameters
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# print(add(a, b))

# def add_numbers(*numbers):
#     return sum(numbers)

# result = add_numbers(1, 2, 3, 4)
# print(result)
# # print(add_numbers(1,2,3,4))


def kwargs_example(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
kwargs_example(name="Alice", age=30, city="New York")


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
# number = int(input("Enter a number to find its factorial: "))    
# print(f"The factorial of {number} is {factorial(number)}")


