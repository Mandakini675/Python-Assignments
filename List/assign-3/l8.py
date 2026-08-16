

# ====================================================================
# 8. Majority Element Detector
# ============================

# Scenario

# Find an element occurring more than N/2 times.

# Requirements

# * Read N and list elements from user
# * Find majority element
# * If not present, display appropriate message

# Test Case 1

# Input:
# [2, 2, 1, 2, 3, 2, 2]

# Output:
# Majority Element = 2

# Test Case 2

# Input:
# [1, 2, 3, 4]

# Output:
# No Majority Element Found

# ---
num =[int(x) for x in input("enter input :").split()]
n = len(num)
major = 1
uniq =[]
for i in range(n):
    if num[i] not in uniq:
        uniq.append(num[i])
        c1 = num.count(num[i])
        if c1>major:
            major=c1
            print("majority element :",num[i])
            break
else:
    print("No Majority Element Found")