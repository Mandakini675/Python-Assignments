"""
===================Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80
------------------------------"""
TOTAL = int(input("enter total marks : "))
obtained = int(input("enter obtained marks :"))
perc = (obtained/TOTAL)*100
print("percentage : ",perc)