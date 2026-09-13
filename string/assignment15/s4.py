'''4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U
'''
s = input("enter string = ").lower()
cons =0

for n in s:
    if n.isalpha():
       if n not in 'aeiou': 
           cons+=1
print(f"Total Consonents:  {cons}")