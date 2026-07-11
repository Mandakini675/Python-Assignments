"""--------------------
Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2
----------------------"""
"""a= int(input("enter 1sub marks:  "))
b = int(input("enter 2sub marks:  "))
c = int(input("enter 3sub marks:  "))
d = int(input("enter 4sub marks:  "))
e = int(input("enter 5sub marks:  "))
"""
a,b,c,d,e= map(int,input("enter sub marks:  ").split(","))


total = a+b+c+d+e
av = (a+b+c+d+e)/5
per = total*100/500

print("Total = ",total)
print("Average = ",av)
print("percentage = ",per)