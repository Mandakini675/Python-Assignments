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
    for ch in s1:
        c1=0
        c2=0
        for j in range(len(s2)):
            if ch==s1[j]:
              c1+=1
        for j in range(len(s2)):
            if ch==s2[j]:
                c2+=1
        if c1!=c2:
            print("Both Product Codes are Not Matching")
            break
    else:
        print("Both Product Codes are Matching")