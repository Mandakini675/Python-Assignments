
# 6.

# NOTE: using tuple only
# An electronics store wants to maintain product information. 
# Since product details should not be modified accidentally,
#  each product record is stored as a tuple.

# Tuple Format:

# (product_id, product_name, price)

# Requirements:

# Read N product details from the user and store them as tuples in a list.
# Display all product details.
# Find and display the costliest product.
# Find and display the cheapest product.
# Calculate and display the average price of all products.
# Display all products whose price is greater than ₹50,000.

# Test Case:

# Input:

# Enter number of products: 4

# P101 Laptop 65000
# P102 Mobile 25000
# P103 Television 80000

# P104 Tablet 30000

# Expected Output:

# All Products:
# ('P101', 'Laptop', 65000)
# ('P102', 'Mobile', 25000)
# ('P103', 'Television', 80000)
# ('P104', 'Tablet', 30000)

# Costliest Product:
# ('P103', 'Television', 80000)

# Cheapest Product:
# ('P102', 'Mobile', 25000)

# Average Price:
# 50000.0

# Products Above ₹50,000:
# ('P101', 'Laptop', 65000)
# ('P103', 'Television', 80000)


n = int(input("enter no of products -----"))
products = []
for i in range(n):
    product_id = input("enter the prod id =")
    product_name = input("enter the prod name =")
    price = int(input("enter the total amount so far ="))
    pr = (product_id,product_name,price)
    products.append(pr)

print("details:")
print("-"*30)
for x in products:
    print(*x)
print("-"*30)

total_amount =0
costliest = products[0][2]
cheap =  products[0][2]
for i in range(n):
    price = products[i][2]

    if price > costliest:
        costliest = price

    if price < cheap:
        cheap = price

    total_amount += price

average = total_amount/n
print("="*30)
print("Costliest Product:")
print(costliest)

print("Cheapest Product:")
print(cheap)

print("Average Price:")
print(average)

print("Products Above ₹50,000:")
for i in range(n):
    if products[i][2] >50000:
        print(products[i])
print("="*30)