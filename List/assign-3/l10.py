
# ====================================================================
# 10. Find Duplicate Numbers
# ==========================

# Scenario

# A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

# Requirements

# * Read N and list elements from user
# * Find all duplicate numbers
# * Store duplicates in another list
# * Count total duplicate numbers
# * Display duplicates in sorted order

# Test Case 1

# Input:
# [1, 2, 3, 2, 4, 5, 1]

# Output:
# Duplicate Numbers = [1, 2]
# Count = 2

# Test Case 2

# Input:
# [10, 20, 30]

# Output:
# No Duplicate Numbers Found

# ---

num =[int(x) for x in input("enter input :").split()]
n = len(num)

uniq =[]
new = []
for i in range(n):
    if num[i] not in uniq:
        uniq.append(num[i])
        c1 = num.count(num[i])
        if c1>1:
            new.append(num[i])
new.sort()
if len(new)>0:
    print("Duplicate numbers:",new)  
    print("count =",len(new))      
else:
    print("No Duplicate Numbers Found")