nums=[1,2,3,4,5,6,7,8,9,4,5,6]
target=9
seen={}                         #seen is to check wether its in the list
for i,num in enumerate(nums):   #enumerate to give index and value
    diff=target-num
    if diff in seen:
        print(seen[diff], i)
    seen[num]=i    
