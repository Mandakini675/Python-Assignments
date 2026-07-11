'''6.
Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191
'''
a = int(input("enter starting number = "))
b = int(input("enter ending number = "))
while a<b:
    temp=a
    rev=0
    while temp>0:
      d=temp%10
      rev = rev*10+d
      temp//=10
    if rev==a:
        print(a)
    a+=1