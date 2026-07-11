'''7.
Neon Number Detector

Scenario:
A smart calculator system checks special numbers used in mathematical testing.
The user enters a range of numbers.
The system identifies all Neon Numbers using nested loops.

Theory:
A Neon Number is a number where the sum of digits of its square is equal to the original number.

Example:
9

Square of 9 = 81

8 + 1 = 9

Since the sum is equal to the original number, 9 is called a Neon Number.

Input:
Enter starting number: 1
Enter ending number: 100

Output:
Neon Numbers are:
1
9
'''
a = int(input("enter starting number = "))
b = int(input("enter ending number = "))
while a<b:
    temp=a  #9
    sum=0
    sqr = a**2  #18
    while sqr>0:
        d=sqr%10
        sum+=d
        sqr//=10
    if sum==a:
        print(a)
        
    a+=1