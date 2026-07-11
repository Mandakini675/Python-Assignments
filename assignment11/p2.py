"""2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4"""
n = int(input("enter number:"))
m = int(input("enter number:"))
count=0

while n<m:
    if n%7==0:
        count+=1
    n=n+1
print("count = ",count)