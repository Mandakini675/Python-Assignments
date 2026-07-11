'''5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3

'''
import math
n= int(input("enter number ="))
t=n
#IF TRUE THEN CHECK FOR NEXT
n=n+1
while True:
    if n<=1:
        n+=1
        continue

    else:
        i=2
        while i<=int(math.sqrt(n)):
           if n%i==0:
             break
           i=i+1
        else:
           print(f"Next Prime ID={n} ")
           break   
    n=n+1
gap=n-t
print(f"gap = {gap}")

  