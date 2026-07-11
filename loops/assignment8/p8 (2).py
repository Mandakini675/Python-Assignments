"""
8. Count Multiples of 5 Between Two Numbers
A supermarket gives coupons to customers whose 
token numbers are multiples of 5.
 The manager enters a token range and wants to
  know how many eligible token numbers exist.
Write a program to count numbers divisible by 5 
between two given numbers using loops.

Input:
1 20

Output:
Count = 4
"""
n1 = int(input("enter number:"))
n2 = int(input("enter number:"))
n=n1
count=0
while n1<=n2:
    if n1%5==0:
        count+=1
    n1=n1+1
print("Count:",count)
    
#-------------->
count1=0
for i in range(n2):
    if n%5==0:
        count1+=1
    n=n+1
print("by foor loop Count:",count1)