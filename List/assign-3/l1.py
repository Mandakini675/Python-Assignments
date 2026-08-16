# ====================================================================

# 1. First Non-Repeating Number
#    ====================================================================

# Scenario

# An online voting system stores vote IDs in a list.

# Find the first vote ID that appears only once.

# Requirements

# * Read N and list elements from user
# * Find the first non-repeating number
# * If no such number exists, display an appropriate message

# Test Case 1

# Input:
# [4, 5, 1, 2, 1, 2, 4]

# Output:
# First Non-Repeating Number = 5

# Test Case 2

# Input:
# [7, 7, 8, 8]

# Output:
# No Non-Repeating Number Found

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
    if count==1:
        print("first non repeating number :",id)
        break
else:
    print("No Non-Repeating Number Found")