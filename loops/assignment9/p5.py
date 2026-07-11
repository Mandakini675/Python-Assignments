'''5.

Automorphic Number Lock

A high-security digital locker validates access codes using a special mathematical rule.

When a user enters a numeric code, the system squares the number and checks whether the last digits of the square match the original number.
 If it matches, the code is considered valid.

An Automorphic Number is a number whose square ends with the same number.

Task:
Write a Python program to check whether a given number is an Automorphic Number or not.

Example:
Input:
25

Output:

automorphic number
'''
n = int(input("enter the no  if aauto Number :"))
sum=0
temp = n
sqr =n**2
while temp>0:
     d=sqr%10
     d2 = temp%10
     if d!=d2:
        print("not")
        break
     temp//=10
     sqr//=10
else:
    print("Automorphic number .")
