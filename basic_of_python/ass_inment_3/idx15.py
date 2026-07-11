"""-----------------------
Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h
-------------------------------"""
dis1 = int(input("enter distance1 : "))
time1 = int(input("enter time1  : "))

dis2 = int(input("enter distance2 : "))
time2 = int(input("enter time2  : "))

s1 = dis1/time1
s2 = dis2/time2

av = (s1+s2)//2

print("Average Speed = ",av," km/h")