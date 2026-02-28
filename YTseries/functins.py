def add(a, b):
    return a + b

# define values for the parameters
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(add(a, b))

def add_numbers(*numbers):
    return sum(numbers)

result = add_numbers(1, 2, 3, 4)
print(result)
# print(add_numbers(1,2,3,4))