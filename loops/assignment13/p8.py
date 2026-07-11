'''ATM Note Counter
A bank ATM dispenses ₹100 notes.
Write a program to:
- Read withdrawal amount
- Count how many ₹100 notes needed using loop

Inpu
700
Output:
Notes = 7
'''
import math
n = int(input("enter withdrawal amount to check how many 100 notes needed :"))
pernote=100
note=0
while n>99:
    n=n-pernote
    note+=1
else:
    print(note)
    
    