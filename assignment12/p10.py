'''Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime
'''
import math
n= input("enter number:")
m = int(n)
sum=0
smallest= 9
z_count=0
z_count = abs(len(str(m))-len(n))
while m>0:
    d=m%10
    if d==0:
        z_count+=1
    else:
        sum=sum+d
    smallest = d if d<=smallest else smallest   
    m//=10
total = sum + z_count    
res = smallest*total
print("Zero Count =",z_count)
print("Sum = ",sum)
print("Smallest Digit =",smallest)
print("Final Result = ",res)
    
if res<=1:
    print("not prime")
else:
    i=2
    while i<int(math.sqrt(res)):
        if res%i==0:
            print("not prime")
            break
        else:
            print("not prime")
            break
        i=i+1