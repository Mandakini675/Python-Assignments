"""5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to *check whether a given number is a palindrome using loops*.

Input: 121
Output: Palindrome"""
n=input("enter number:")
rev=""
for i in n:
    rev = i+rev
if rev==n:
    print("palindrome")
else:
    print("not")
