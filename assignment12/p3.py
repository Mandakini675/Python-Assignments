'''3. Composite Number Detector

A product testing company labels batch numbers as risky 
if they have more than two factors. Such numbers are known as
 composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and 
the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number'''
n= int(input("enter number: "))
flag=0
i=1
#while i<int(math.sqrt(n)):
while i<=n//2:
    if n%i==0:
        flag+=1
    if flag>2:
        print("Composite Number")
        break
    i+=1
else:
    print("not a composite number")


    