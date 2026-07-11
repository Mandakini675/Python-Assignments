'''.Unique Digit Security Scanner

A smart locker accepts only numbers whose all digits are unique.
Write a program using for-else loop to:
- Check every digit
- If any repeated digit found reject
- Else accept
Input:
57294

Output:
Valid Unique Code
'''
m= input("enter number :")
n=int(m)
l=len(str(m))
freq=0
for i in range(1,l+1):
    d = n%10
    for j in m:
        if d==int(j):
            freq+=1
    if freq>1:
        print("NOT Valid ")
        break
    else:
        freq=0
    n//=10
else:
    print("Valid Unique Code")
     

       