'''8.
Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number
'''
n = int(input("enter if no is trimorphic num: "))
temp = n
cube = n**3
while temp>0:
    if temp%10 != cube%10 :
      print("not")
      break
    temp//=10
else:
   print("Trimorphic Number")
     