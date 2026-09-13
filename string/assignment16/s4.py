'''
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID

'''
s = input("Enter Employee ID: ")

if len(s)==8 and s[ :3]=="EMP" and s[3: ].isdigit():
    print("Valid Employee ID")
else:
    print("not Valid Employee ID")