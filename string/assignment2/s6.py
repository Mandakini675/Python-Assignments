'''
6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching

'''
s1 = input("Enter first product code: ").lower().replace(" ", "")
s2 = input("Enter second product code: ").lower().replace(" ", "")

if len(s1) != len(s2):
    print("Both Product Codes are Not Matching")

else:
    match = True
    for p in s1:

        for j in range(len(s)):
            