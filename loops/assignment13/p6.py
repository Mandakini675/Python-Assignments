'''Next Prime Cabin Number Generator
A luxury hotel gives only prime numbered cabins to VIP guests.
Manager enters the last allotted cabin number.
System must find the next available prime cabin number.

Write a program using loops.
Input:
24
Output:
Next Prime Cabin = 29

'''
import math
n= int(input("enter code: "))
n=n+1
while True:
    if n<=1:
        n+=1
        continue
    i=2
    while i<=int(math.sqrt(n)):
        if n%i==0:
          break
        i=i+1
    else:
        print(f"Next Prime Cabin = {n} ")
        break   
    n=n+1