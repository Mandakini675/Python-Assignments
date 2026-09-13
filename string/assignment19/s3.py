'''
3.
Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda
'''
s=input("enter string: ")
sing_ch=s[0]
for i in range(1,len(s)):

    if s[i]==s[i-1]:
        continue
    sing_ch+=s[i]
print(sing_ch)