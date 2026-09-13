'''
3. Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output:


e
'''
s=input("enter the string:")
freq=0
for i in range(len(s)):
    
    for ch in s:
        if s[i]==ch:
            freq+=1
    if freq<=1:
        print(s[i])
        break
    freq=0
else:
    print("no repeated character found")