'''1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username
'''
s=input("enter username =")
valid = True
if 5<=len(s)<=12 and s[0].isalpha():
    for ch in s:
        if not (ch.isalnum() or ch == "_"):
            valid = False
            break             
else:
    valid = False


if valid:
    print("Valid Username")
else:
    print("NOT Valid Username")
    