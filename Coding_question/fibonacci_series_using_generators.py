def fibonacci(n):    #Formula (Conceptual)F(n) = F(n-1) + F(n-2)
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
for num in fibonacci (50):
    print(num)