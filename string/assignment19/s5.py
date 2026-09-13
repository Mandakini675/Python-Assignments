'''
5.
Cybercrime Log Analysis System

A cybersecurity company monitors encrypted login activity stored as character-based security logs.

During investigation, analysts need to identify the last character that repeats in the log sequence.
This helps detect the most recent duplicated activity pattern before a possible security breach.

Write a Python program to find the last repeating character in a given string.

If no repeating character exists, print:

No repeating character found
Input:
abccdbefga
Output:
a'''
s= input("enter the string:")
count=0

for i in range(len(s)):
    if s[i]==s[-1]:
        count+=1
if count>1:
    print(s[-1])
else:
    print("No repeating character found")