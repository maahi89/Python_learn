# square pattern
for i in range(4):
    for j in range(4):
        print("* ", end="")
    print()
print("----------------------------------------------")

# right angle triangle pattern
for i in range(4):
    for j in range(i+1):
        print("* ", end="")
    print()
print("----------------------------------------------")


# inverted right angle triangle pattern
for i in range(4):
    for j in range(4-i):
        print("* ", end="")
    print()
print("----------------------------------------------")


# hollow square pattern
for i in range(4):
    for j in range(4):
        if i==0 or i==3 or j==0 or j==3:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
print("----------------------------------------------")


# number pattern 
n =5
for i in range(1, n+1):
    for j in range(1, i+1):
        print( j, end="")
    print()
print("----------------------------------------------")


# pyramid pattern
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
print("----------------------------------------------")
