"""Count Odd Digits*
A banking system flags IDs with too many odd digits 
for further verification.
Write a program to *count the number of odd digits 
in a given number using loops*.

Input: 123456
Output: Odd digits count = 3
"""
n = int(input("enter number :"))
count=0
while n>0:
    digit= n%10
    if digit%2==0:
       pass
    else:
      count+=1
    n=n//10

print("Even digits count =",count)