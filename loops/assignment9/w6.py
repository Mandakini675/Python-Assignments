"""
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique.
 A 3-digit Armstrong number is one where the sum of the cubes
  of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong
"""
n = int(input("enter number :"))
num=n
sum=0
i=1
while n>0:
   digit= n%10
   cube=digit**3
   n=n//10
   sum=sum+cube

if sum==num:
    print("Armstrong")
else:
     print("not a Armstrong")