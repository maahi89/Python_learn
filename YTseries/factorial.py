def factorial(n):
    res=1
    for i in range(1, n+1):
        res *= i
    return res
number = int(input("Enter a number to find its factorial: "))           
print(factorial(number))