'''9.
Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12

Output:
Abundant Number
'''
n= int(input("enter number if abundant ="))
sum=0
i=1
while i<n:
    if n%i==0:
       sum+=i
    i+=1
if sum>n:
    print("Abundant Number")
else:
    print("not")