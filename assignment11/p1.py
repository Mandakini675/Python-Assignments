"""1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd 
numbers up to n.
Write a program using loops to find product 
of odd numbers.

Input:
5

Output:
15
"""
n = int(input("enter number:"))
mul=1
i=0
while i<n:
    i=i+1
    if i%2==0:
        continue
    mul*=i
print(mul)
#------------->
m = int(input("enter number:"))
mulp=1
for x in range(1,m+1):
    if x%2==0:
        continue
    mulp*=x
print(mulp)