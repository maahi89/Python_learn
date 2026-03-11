num=(5,3,5,66,37,88,99,100,11)
print(num[1])
print(num)
print(num[1:5])
print(num[5:])
print(num[:5])  
print(num[-5:])
print(num)


set1={1,2,3,4,5,5}
set2={4,5,6,7,8}    
print(set1)
print(set2)
print(set1.union(set2))
print(set1.intersection(set2))
set1.add(77)
# set1.remove(2)
print(set1.add(frozenset(set2)))
print(set1)
