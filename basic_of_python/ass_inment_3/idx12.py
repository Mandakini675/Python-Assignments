"""---------------------------
assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3
------------------------------"""
amount = int(input("enter total amount :"))
for100 = amount//100
for50 = (amount%100)//50
for10  = ((amount%100)%50)//10

print("₹100 * ",for100," ,₹50 * ",for50," ,₹10 * ",for10)