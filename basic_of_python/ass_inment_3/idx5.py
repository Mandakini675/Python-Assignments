"""-----------------------------------------------
Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
------------------------------------------------------------"""
print("here calculate average your 3 subject marks")
a = int(input("Enter marks:chem  "))

b = int(input("Enter marks:physics  "))

c = int(input("Enter marks:maths  "))
av = (a+b+c)/3
print("Average = ",av)