"""
10. Even Numbers Between Two Numbers*
A teacher wants to assign only even roll numbers for 
a special activity. The system should display all 
qeven numbers between two given numbers.
Write a program to *display all even numbers between
 two numbers using loops*.

Input: 10, 20
Output: 10 12 14 16 18 20
"""
a,b = map(int,input("enter two range digit:").split(","))
if a<b and a%2==0:
    for i in range(a,b+1,2):
        print(i,end=" ")
else:
    pass

