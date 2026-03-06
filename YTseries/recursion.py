# def count(n):
#     if n == 0:
#         return 
#     print(n)
#     count(n-1)
# print(count(7))


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))