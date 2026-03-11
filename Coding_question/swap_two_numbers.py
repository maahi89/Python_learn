# without using temp
# a=10
# b=20
# a,b=b,a
# print(a,b)


#Using temp
a=10
b=20
temp=a
a=b
b=temp
print(a,b)