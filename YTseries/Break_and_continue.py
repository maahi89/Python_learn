x= int(input("enter the number of chocolates: "))
available = 10
i=1
while i<=x:
   if i > available:
      break

   print("chocolate")
   i += 1

print("no more chocolates available")

print("--------------------------------------------------")  

for i in range(1, 100):
    if i % 2 == 0 and i % 5 == 0:
        continue
    print(i)
print("--------------------------------------------------")


# print even numbers from 1 to 100
for i in range(1, 100):
    if i % 2!= 0:
        continue
    print(i)    