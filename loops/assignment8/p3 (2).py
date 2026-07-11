"""
3. First Digit of Number
A university receives thousands of application IDs. The first digit of each ID represents the department code, 
so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5
"""
n = int(input("enter number:"))
num = n
while n>0:
    d= n%10
    if n<=9:
        first = n
    n=n//10
print("First Digit = ",first)
l = len(str(num))
for i in range(l):
    d= num%10
    if i==(l-1):
        first = num
    num=num//10
print("by for loop First Digit = ",first)