'''
5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password
'''
s = input("enter password = ")
digit = 0
special = False
space = False
digit_count = 0
upper = False
last_digit = False

if (8 <= len(s) <= 15 and s[0].isupper() and s[-1].isdigit() ):
    upper = True
    last_digit=True
    for ch in s:
        if ch.isdigit():
            digit_count += 1
        if ch in "@#$%&*":
            special = True
        if ch.isspace():
            space = True
    if upper and last_digit and digit_count >= 2 and special and not space:
        print("Secure Password")
    else:
        print("Not Secure Password")

else:
    print("Not Secure Password")