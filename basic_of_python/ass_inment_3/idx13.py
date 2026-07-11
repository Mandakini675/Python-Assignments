"""------------------------------
Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0
--------------------------"""
p = int(input("Enter principle  "))
r = int(input("Enter rate  "))

t = int(input("Enter time  "))
A = p*(1 + r/100)**t
CI = A-p
print("Amount = ",A)
print("Compound Interest = ",CI)


