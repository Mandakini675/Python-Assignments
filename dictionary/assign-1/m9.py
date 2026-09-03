
# 9.

# =========================================
# INVENTORY MANAGEMENT SYSTEM
# ===========================

# Store product stock in a dictionary.

# stock = {
# "Pen":50,
# "Pencil":100,
# "Eraser":25,
# "Marker":10
# }

# Write a program to:

# * Display products having stock less than 30.

# Sample Output:
# Eraser
# Marker

# ---
print("===========================")
print("  INVENTORY MANAGEMENT SYSTEM")
print("============================")


stocks = input("enter products name :").split()
price = input("enter prices of each resp.. name :").split()

products = {}

for x,y in zip(stocks,price):
    products[x] = int(y)
print("~~~~~~~~~~")
for x in products:
    if products[x]<30:
        print(x)
   