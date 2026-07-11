'''7.
Adam Number Verification System – Question

A high-security digital system is designed to validate special mirrored numbers known as Adam Numbers before granting access to sensitive data.

When a user enters a numeric code, the system performs a dual verification process:

* It calculates the square of the entered number.
* It reverses the number and calculates the square of the reversed value.
* Finally, it checks whether both results are mirror images (reverses) of each other.

A number is called an Adam Number if:
The square of the number and the square of its reverse are reverses of each other.

Task:
Write a Python program to check whether a given number is an Adam Number or not.

Examples:

Input:
12
Output:
Adam Number

Input:
13
Output:
Not an Adam Number

Input:
11
Output:
Adam Number

Example:
12 → 12² = 144, reverse(12) = 21 → 21² = 441 → reverse of 144'''

n = int(input("enter if the number is adam or not :"))
temp=n
r_v=0
sqr = n**2
#reverse the num
while n>0:
    d=n%10
    r_v=r_v*10+d
    n//=10

#squRE OF REVERSED  number
sq_rev = r_v**2

rev =0


while sq_rev>0:
    d=sq_rev%10
    rev=rev*10+d
    
    sq_rev//=10

if sqr==rev:
    print("Adam number")
else:
    print("not")