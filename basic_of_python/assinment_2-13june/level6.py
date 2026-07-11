"""========================================
Assignment 6: Smart Coin Machine
========================================

You insert an amount into a vending machine. It returns coins using the largest denominations possible (₹10 and ₹5).

Write a Python program that:
- Accepts the total amount.
- Calculates how many ₹10 coins and ₹5 coins will be dispensed.
- Displays the result.

Example:
Amount = ₹35
Output = ₹10 x 3, ₹5 x 1
"""
amount = int(input("enter total amount :"))
ten = amount//10
fives = (35%10)//5
print("Amount = ",amount)
print("output = 10 *",ten,",5 * ",fives)