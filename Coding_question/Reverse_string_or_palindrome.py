# name="mahitha"
# print(name[::-1])

name="mahitha"
rev=""
for i in name:
    rev=i+rev
print(rev)    

name = "madam"
if name == name[::-1]:
    print(f"{name} is a palindrome")
else:    
    print(f"{name} is not a palindrome")

name = "Rahul"
print(name[::-1])
print(name[0:2])
print(name[-1:-3:-1])