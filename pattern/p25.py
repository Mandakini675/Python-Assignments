n = int(input("Enter number: "))
i= 1
while i<=n:
   j=n
   while j>n-i:
       print(j,end="")
       j-=1
   i+=1
   print()

# Enter number: 5
# 5
# 54
# 543
# 5432
# 54321