
# ====================================================================
# 4. max_chain e st Consecutive Sequence
# ===============================

# Scenario

# Find the max_chain e st sequence of consecutive numbers present in the list.

# Requirements

# * Read N and list elements from user
# * Find the length of the max_chain e st consecutive sequence
# * Display the sequence length

# Test Case 1

# Input:
# [100, 4, 200, 1, 3, 2]

# Output:
# max_chain e st Consecutive Length = 4

# Explanation:
# Sequence = 1, 2, 3, 4

# Test Case 2

# Input:
# [10, 11, 12, 20]

# Output:
# max_chain e st Consecutive Length = 3

# ---😑

el = [int(x) for x in input("input :").split()]
el.sort()
chain=1
max_chain = 1
for i in range(1,len(el)):
    if el[i]-el[i-1]==1:
        chain+=1
    else:
        chain=1
    if chain>max_chain : 
        max_chain = chain
print(max_chain ) 