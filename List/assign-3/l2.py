
# ====================================================================
# 2. First Repeating Number
# =========================

# Scenario

# A security system logs employee IDs.

# Find the first ID that repeats in the list.

# Requirements

# * Read N and list elements from user
# * Find the first repeating number
# * If no repeating number exists, display an appropriate message

# Test Case 1

# Input:
# [10, 5, 3, 4, 3, 5]

# Output:
# First Repeating Number = 3

# Test Case 2

# Input:
# [1, 2, 3, 4]

# Output:
# No Repeating Number Found

# ---
n= int(input("enter no of ids :"))
lst=[]
for i in range(n):
    lst.append(input())

for i in range(n):
    id = lst[i]
    count=0
    j=0
    while j<n:
       if id ==lst[j]:
         count+=1
       j+=1
    if count>1:
        print("first repeating number :",id)
        break
else:
    print("No Repeating Number Found")