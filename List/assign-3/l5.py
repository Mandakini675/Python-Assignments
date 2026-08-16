# ====================================================================
# 5. Equilibrium Index Finder
# ===========================

# Scenario

# Find an index where:

# # Sum of elements on the left side

# Sum of elements on the right side

# Requirements

# * Read N and list elements from user
# * Find equilibrium index
# * If not found, display message

# Test Case 1

# Input:
# [1, 3, 5, 2, 2]

# Output:
# Equilibrium Index = 2

# Explanation:
# 1 + 3 = 2 + 2

# Test Case 2

# Input:
# [1, 2, 3]

# Output:
# No Equilibrium Index Found

# ---will do ot later😭
num = [int(x) for x in input("input here :").split()]
n=len(num)
sm1=0
sm2 =0
i = 0
end=n
while  i< end:
    
    sm1 = sm1+num[i]
    sm2 = sm2+num[end-1]
    # if sm1==sm2:
    #     print(i+1)
        # break
    end-=1
    i+=1
if sm1==sm2:
   print(i+1)