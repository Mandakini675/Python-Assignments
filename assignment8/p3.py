'''3.
Prime Number Range Checker

A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.

Input:
Enter starting number: 10
Enter ending number: 50

Output:
Prime Numbers are:
11
13
17
19
23
29
31
37
41
43
47
'''
import math
a = int(input("enter starting number = "))
b = int(input("enter ending number = "))
while a<b:
    if a>1:
        i=2
        while i<=int(math.sqrt(a)):
            if a%i==0:
                break
            i+=1
        else:
            print(a)
    a+=1