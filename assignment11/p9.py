"""Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number
"""
#my approach
m= int(input("enter id number:"))
l=len(str(m))
sum=0
max=0
#for reverse
n=0
while m>0:
    n=n*10+m%10
    m=m//10
print(n)
#finding adjacent diff
while n>=10:
    last=n%10
    n=n//10
    seclast = n%10
    diff = seclast-last if seclast>last else last-seclast
    seclast=last
    print(diff,end=" ")
    max = max if max > diff else diff
    sum=sum +diff

print(f"\nsum = {sum}")
print("largest difference = ",max)
if sum%l==0:
    print("Balanced Number")
else:
    print("Unbalanced Number")

'''
n= int(input("enter id number:"))
temp=n
store=""
l=len(str(n))
sum=0
max=0
last = n%10
n=n//10
while n>0:
    seclast=n%10
    diff=seclast-last if seclast>last else last-seclast
    sum+=diff
    max=max if max>diff else diff
    
    store+=str(diff)
    n=n//10
    last = seclast

# print(store)
print(f"sum : {sum}")
print(f"max : {max}")
    
store1=int(store)
rev=0

while store1>0:
    d=store1%10
    rev=rev*10+d
    store1//=10

print(f"Step Differences: {rev}")'''
