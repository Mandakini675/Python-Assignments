""". Check All Digits Are Even*
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
"""
n = int(input("enter number :"))
count=0
while n>0:
    digit= n%10
    if digit%2==0:
       count=0
    else:
      count+=1
    n=n//10
if count==0:
    print("All even")
else:
    print(" All not even")