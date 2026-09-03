
# 12.

# =========================================
# ONLINE FOOD DELIVERY ANALYSIS
# =============================

# orders = [
# "Pizza",
# "Burger",
# "Pizza",
# "Pasta",
# "Burger",
# "Pizza",
# "Pasta"
# ]

# Write a program to:

# * Count orders of each food item.
# * Find the most ordered item.

# Sample Output:
# Pizza : 3
# Burger : 2
# Pasta : 2

# Most Ordered : Pizza

# ---


print("===========================")
print("  INVENTORY MANAGEMENT SYSTEM")
print("============================")


orders = input("enter items name :").split()

ordrd = {}

for x in orders:
    if x in ordrd:
       ordrd[x] += 1
    else:
        ordrd[x] = 1
print("~~~~~~~~~~")
high = max(ordrd.values())
for k,v in ordrd.items():
    if ordrd[k]==high:
        print("Most ordered ",k,":",v)
  