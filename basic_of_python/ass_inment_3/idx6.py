"""------------------------------------------------------------
Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900
----------------------------------------------------------------"""
amount = int(input("amount :"))
dis10 = (10/100)*amount
final = amount - dis10
print("Discount = ",dis10)
print("FInal = ",final)