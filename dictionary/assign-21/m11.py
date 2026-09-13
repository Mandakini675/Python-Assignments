
# 11.

# =========================================
# PRODUCT SALES ANALYSIS
# ======================

# sales = [
# "Mobile",
# "Laptop",
# "Mobile",
# "Tablet",
# "Laptop",
# "Mobile"
# ]

# Write a program to:

# * Count sales of each product.
# * Display products in sorted order.

# Sample Output:
# Laptop : 2
# Mobile : 3
# Tablet : 1

# ---

print("===========================")
print("  INVENTORY MANAGEMENT SYSTEM")
print("============================")


stocks = input("enter products name :").split()

sales = {}

for x in stocks:
    if x in sales:
       sales[x] += 1
    else:
        sales[x] = 1
print("~~~~~~~~~~")
print(sales)
for k,v in sorted(sales.items()):
    
        print(k,":",v)
  