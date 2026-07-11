'''2. Multi Stage Prime Lock System
A smart locker opens only if final derived number is prime.
Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not
Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime

'''
import math
n = int(input("enter input number :"))
prod=1
sum=0
temp = n
for i in range(len(str(n))):
    d=n%10
    prod*=d
    sum+=d
    n//=10
#Find difference between product and sum
diff = abs(prod-sum)
d_ff = diff
dig=0
print(len(str(diff)))
#Count digits in difference
for i in range(len(str(diff))):
    dd=diff%10
    dig =dig+1
    diff//=10
final= d_ff+dig

print("Sum =",sum)
print("product = ",prod)
print("Difference = ",d_ff)
print("Digits =",dig)
print("Final Result = ",final)
