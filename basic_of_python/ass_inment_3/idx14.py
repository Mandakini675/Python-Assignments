"""------------------------------
Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0
-----------------------"""
cost_price = int(input("enter cost price :"))

selling_price = int(input("enter selling price :"))

profit = selling_price - cost_price

profit_perc = (profit/cost_price)*100
print("Profit = ",profit)
print("Profit % = ",profit_perc)
