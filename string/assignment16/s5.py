'''
5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code'''
s = input("Enter product code:")
rev=""
for ch in s:
    rev = ch+rev
if s==rev:
    print("Palindrome Code")
else:
    print("not Palindrome Code")