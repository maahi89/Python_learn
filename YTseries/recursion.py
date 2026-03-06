def count(n):
    if n == 0:
        return 
    print(n)
    count(n-1)
print(count(7))