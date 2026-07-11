'''Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime
'''
import math
n = int(input("enter number: "))
ecount = 0
ocount =0
while n>0:
    d=n%10
    if d%2==0:
        ecount+=1
    else:
        ocount+=1
    n//=10
diff = ecount-ocount if ecount>ocount else ocount-ecount
print("Even Count =",ecount)
print("Odd Count = ",ocount)
print("Difference = ",diff)

if diff<=1:
    print("not prime")
else:
    i=2
    while i<int(math.sqrt(diff)):
        if diff%i==0:
            print("not prime")
            break
        else:
            print("not prime")
            break
        i=i+1