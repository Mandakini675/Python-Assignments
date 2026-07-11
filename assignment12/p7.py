'''7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number
'''
import math
m = int(input("enter number: "))
sum=0
for i in range(m):
    d= m%10
    sum+=d
    m//=10
print("sum = " ,sum)

if sum<=1:
    print("Normal Number")
else:
    i=2
    while i<=int(math.sqrt(n)):
        if sum%i==0:
            print("normal number ")
            break
        i+=1
    else:
            print("Lucky Number")    
