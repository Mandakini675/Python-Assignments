"""4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
"""
m = int(input("enter number:"))
temp=m
l= len(str(m))
sum=0
fact=1
for j in range(l):
    d=m%10
    for i in range(1,d+1):
        fact*=i
    print(fact)
    sum=sum+fact
    fact=1
    m//=10
else:
    if sum==temp:
        print("strong number")
    else:
        print("not a stronng num")