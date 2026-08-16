

# =====================================================================
# QUESTION 4: ONLINE ordersPING ORDERS
# ==================================
# An online ordersping company stores customer orders using NamedTuple.
# Fields:
# order_id, customer_name, product_name, amount
# Requirements:
# 1. Read N order records from the user and store them in a list of NamedTuples.
# ---
# 2. Display all order details.
# ---
# 3. Find and display the order having the highest_orderest amount.
# ---
# 4. Calculate and display total sales.
# ---
# 5. Count the number of orders whose amount is greater than ₹10,000.

# Test Case:

# Input:
# Enter number of orders: 5

# O101 Rahul Laptop 55000
# O102 Priya Mouse 800
# O103 Amit Mobile 25000
# O104 Neha Keyboard 1500
# O105 Rakesh TV 45000

# Expected Output:
# highest_orderest Value Order:
# O101 Rahul Laptop 55000

# Total Sales:
# 127300

# Orders Above ₹10,000:
# 3

from collections import namedtuple
print("====================================================================")
print("           ONLINE SHOPPING  ORDERS")
print(" ==================================================================")

n = int(input("Enter number of orders:"))

Order = namedtuple("orders",["order_id", "customer_name", "product_name", "amount"])
orders = []
for i in range(n):
    order_id = input("enter order id =")
    name = input("enter customer name = ")
    prod_name = input("enter product name = ")
    amount= int(input("enter amount ="))
    prd1 = Order(order_id,name ,prod_name,amount)
    orders.append(prd1)
print("details :")
print("-"*20)
for x in orders:
    print(*x)
print("-"*20)

highest_order = orders[0]
total_sales = 0
count =0
for order in orders:
    if order.amount > highest_order.amount:
        highest_order = order
    if order.amount>10000:
        count += 1
    total_sales += order.amount

print("-"*20)
print("highest_orderest value order :")
print(*highest_order)

print("Total Sales:")
print(total_sales)

print("Orders Above ₹10,000:")
print(count)
print("-"*20)