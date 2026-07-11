'''Number Stability Analyzer
A science lab studies whether digits are in increasing order.
Write a program using for-else loop:
- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number
'''
n= int(input("enter number :"))
for i in range(1,n+1):
    last=n%10
    n//=10
    seclast = n%10
    if last<seclast:
        print("not a stable number")
        break
else:
    print("stable number")
    