'''6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2
'''
import math
n= int(input("enter number: "))
flag=0
i=1
small=float('inf')
#while i<int(math.sqrt(n)):
while i<=n:
    if n%i==0:
        flag+=1
    if i>1:
        small = i if i<small else small
    i+=1

if flag>2:
        print("Composite Number")
else:
    print("not a composite number")

print("Factors Count =",flag)
print(f"Smallest Factor = {small}")