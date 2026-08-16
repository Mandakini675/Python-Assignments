
# 6.

# A security system logs employee entry IDs during a day.

# Only prime-numbered IDs are considered valid VIP entries.

# Tasks:

# Extract all prime IDs from the list
# Find the sum of prime IDs
# Find the maximum prime ID
# Count how many prime entries exist

# Input:
# A list of integers (may contain duplicates and non-prime numbers)

# Example 1

# Input:
# [12, 5, 7, 9, 11, 14, 17]

# Output:
# Prime IDs = [5, 7, 11, 17]
# Sum = 40
# Max = 17
# Count = 4

# Example 2

# Input:
# [4, 6, 8, 10]

# Output:
# Prime IDs = []
# Sum = 0
# Max = -1
# Count = 0



import math
n=int(input("enter the no of IDs: "))

l1=[]
prim=[]

for i in range(n):
     l1.append(int(input()))
  
for i in range(len(l1)):
    if l1[i]>1:
        j=2
        while j<=int(math.sqrt(l1[i])):
            if l1[i]%j==0:
                j+=1
                break
            j+=1
        else:
            prim.append(l1[i])
total=sum(prim) 
print(f"Prime IDs = [{prim}]")
print(f"sum = {total}")
if len(prim)>0:
    print("max =",max(prim))
    
else:
    print("Max = -1",)  
print("count = ",len(prim))  

