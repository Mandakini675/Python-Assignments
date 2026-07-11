"""------------------------
Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750
-----------------------------"""
hrs = int(input("Enter HOURS  "))

min = int(input("Enter MINUTES  "))

sec = int(input("Enter SECONDS  "))
 
total = sec + (min*60)+(hrs*3600)

print("Total seconds  : ",total)