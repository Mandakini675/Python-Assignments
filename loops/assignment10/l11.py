"""
Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.

Input: Number = 122312, Digit = 2
Output: 3
"""
n = input("enter number :")
dig= int(input("enter freq to which num check :"))
freq=0
"""for i in range(0,n+1):
    digit = n%10
    if digit==dig:
         freq+=1
    n=n//10"""
for ch in n:
    if ch == str(dig):
        freq += 1
print(freq)