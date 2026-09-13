'''2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST
'''
s=input("Enter employee name: ")
ans=""
for i in range(len(s)):
    if i==0 and "a"<=s[i]<="z":
        ans+=chr(ord(s[i])-32)
        continue
    if s[i-1]==" " and "a"<=s[i]<="z":
        ans+=chr(ord(s[i])-32)
print("Employee Short ID:",ans)
