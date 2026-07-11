'''.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number
'''
n = int(input("enter the no if it's Spy Number :"))
sum=0
temp = n
prod=1

while temp>0:
    d= temp%10
    prod*=d
    sum+=d
    temp//=10
if prod == sum:
    print("Spy number")
else:
    print("not")
    