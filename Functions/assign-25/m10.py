# 6.
#  Mobile Recharge System

# A telecom company issues lucky recharge coupons only if the coupon number is prime.

# Task

# Write a recursive function to determine whether a given number is prime.

# Input
# Enter Coupon Number:
# 29
# Output
# Prime Number
import math
def prime(num,i):
    if num < 2:
        return False
    if i*i>num:
        return True
    if num%i==0:
        return False
    return prime(num,i+1)

number = int(input("enter coupen number:"))
if prime(number,2)==True:
    print("PRIME number")
else:
    print("NOT PRIME")