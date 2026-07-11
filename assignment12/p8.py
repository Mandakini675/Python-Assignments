'''8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime
'''
import math
n = int(input("enter number: "))
largest = 0
smallest = float('inf')
while n>0:
    d=n%10
    largest = d if d>largest else largest
    smallest = d if d<smallest else smallest
    n//=10
sum= smallest+largest
print("Largest =",largest)
print("Smallest = ",smallest)
print("Sum = ",sum)
if sum<=1:
    print("Not Prime")
else:
    i=2
    while i<=int(math.sqrt(sum)):
        if sum%i==0:
            print("Not prime number")
            break
        else:
            print("Prime number")
            break