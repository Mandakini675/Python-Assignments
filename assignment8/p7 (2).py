"""7. Power of a Number
A scientific calculator app is used by engineering 
students for repeated multiplication operations. 
It should calculate the value of a number raised 
to a given power.
Write a program to calculate n raised to power 
p using loops.

Input:
2 5

Output:
32
"""
n = int(input("enter number:"))
a= int(input("enter number:"))
power=1
for i in range(0,a):
    power=power*n
print(power)
#------------->
por=1
i=1
while i<a :
    por=por*n
    i+=1
print("by while loop",power)