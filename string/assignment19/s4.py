'''
4.

Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d'''

s= input("enter the string:")
uniq=""
high=0
count=0
h_v=""

for ch in s:
    count=0
    if ch in uniq:
        continue
    uniq+=ch

    for c in s:
        if ch==c:
            count+=1

    if count>=high:
        if count > high:
             high = count
             h_v = ch          # Reset
        elif count == high:
            h_v += ch         # Append

print(h_v)