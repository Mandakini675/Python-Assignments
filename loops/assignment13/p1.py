'''1. Triple Operation Prime Verification System
A cybersecurity company generates a security score from entered access code.
Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime
'''
import math
n = int(input("enter input number :"))
rev=0
sum=0
temp = n
for i in range(len(str(n))):
    d=n%10
    rev = rev*10+d
    sum+=d
    n//=10
diff = abs(rev -temp)
final = diff + sum
print("Sum of Digits",sum)
print("Reverse = ",rev)
print("Difference = ",diff)
print("Final Result = ",final)

if final<=1:
    print("not prime")
else:
    i=2
    while i<int(math.sqrt(final)):
        if final%i==0:
            print("not prime")
            break
    else:
        print("prime number")
