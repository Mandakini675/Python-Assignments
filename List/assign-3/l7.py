
# ====================================================================
# 7. Array Rotation Analyzer
# ==========================

# Scenario

# Rotate the array K times towards the right.

# Requirements

# * Read N and list elements from user
# * Read K
# * Rotate the array
# * Display rotated array

# Test Case 1

# Input:
# Array = [1, 2, 3, 4, 5]
# K = 2

# Output:
# [4, 5, 1, 2, 3]

# Test Case 2

# Input:
# Array = [10, 20, 30, 40]
# K = 1

# Output:
# [40, 10, 20, 30]

# ---

num =[int(x) for x in input("enter input :").split()]
n = len(num)
k=int(input("enter how many times want"))
# hold = num[n-1]
for itr in range(k):
    hold = num[n-1]
    for i in range(len(num)-1,0,-1):
      num[i]=num[i-1]
    
    num[0]=hold
print(*num)
    

       
# num =[int(x) for x in input("enter input :").split()]
# n = len(num)
# k=int(input("enter how many times want to"))
# newlist = []
# newlist = [num[n-1]]
# for i in range(len(num)-1):
#     newlist.append(num[i])
# print(*newlist)
    