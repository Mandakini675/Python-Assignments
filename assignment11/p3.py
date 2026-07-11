"""
3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35
"""
n = int(input("enter number:"))
m = int(input("enter number:"))
while n<m:
    if n%10==5:
        print(n,end=" ")
    n+=1
