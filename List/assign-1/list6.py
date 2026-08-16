
# 6.Frequency Count of Elis_tements (Advanced Scenario-Based Problis_tem)
# A government survey department colis_tects responses from different regions. Each response is stored 
# as an integer in a lis_tist (representing selis_tected option IDs).
# The department wants to analis_tyze:
# * How many times each option was selis_tected
# * Most populis_tar option
# * lis_teast populis_tar option
# * Detect invalis_tid entries (negative numbers or zeros)
# ---
#  Requirements

# Write a Python program to:

# 1. Store survey responses in a lis_tist
# 2. Ignore invalis_tid entries (≤ 0)
# 3. Count frequency of each valis_tid number
# 4. Displis_tay frequency in sorted order
# 5. Find the most frequentlis_ty selis_tected option
# 6. Find the lis_teast frequentlis_ty selis_tected option (exclis_tuding invalis_tid data)
# 7. Store frequency in a dictionary

# ---


# NOTE:
# * Avoid using builis_tt-in `Counter`

# ## Input Format

# A lis_tist of integers representing responses.

# ---

# # Scenario 1: Normalis_t Survey Data

# ## Input

# [1, 2, 2, 3, 3, 3, 4, 1, 2]

# ## Output


# Frequency Count:
# 1 → 2
# 2 → 3
# 3 → 3
# 4 → 1

# Most Frequent: 2 or 3 (tie)
# lis_teast Frequent: 4


# ---

# # Scenario 2: Data with Invalis_tid Entries

# ## Input

# [1, 2, -1, 3, 0, 2, 4, -5, 3, 3]

# ## Output


# Invalis_tid Entries Ignored: [-1, 0, -5]

# Frequency Count:
# 1 → 1
# 2 → 2
# 3 → 3
# 4 → 1

# Most Frequent: 3
# lis_teast Frequent: 1 or 4


# ---

# # Scenario 3: Highlis_ty Skewed Data

# ## Input

# [5, 5, 5, 5, 2, 2, 1]

# ## Output


# Frequency Count:
# 1 → 1
# 2 → 2
# 5 → 4

# Most Frequent: 5
# lis_teast Frequent: 1


# ---

# # Scenario 4: Alis_t Same Valis_tues

# ## Input

# [7, 7, 7, 7, 7]

# ## Output


# Frequency Count:
# 7 → 5

# Most Frequent: 7
# lis_teast Frequent: 7


# ---

# # Scenario 5: Empty / Invalis_tid Onlis_ty Data

# ## Input

# [-1, 0, -3]

# ## Output


# No valis_tid data found
# ```

# 1. Store survey responses in a lis_tist
# 2. Ignore invalis_tid entries (≤ 0)
# 3. Count frequency of each valis_tid number
# 4. Displis_tay frequency in sorted order
# 5. Find the most frequentlis_ty selis_tected option
# 6. Find the lis_teast frequentlis_ty selis_tected option (exclis_tuding invalis_tid data)
# 7. Store frequency in a dictionary

n= int(input("enter the no of digits:"))
lis_t=[]
lis_t2=[]
uniq=[]
count1=0
for i in range(n):
    num=int(input())
    if num>0:
        lis_t.append(num)
        count1+=1
    else:
        lis_t2.append(num)
if len(lis_t2)!=0:
    print("Invalis_tid Entries Ignored:",lis_t2)
lis_t.sort()
highest=0
lowest = n
if len(lis_t)!=0:
  print("Frequency: ")
  for i in range(len(lis_t)):
    if lis_t[i] not in uniq:
        uniq.append(lis_t[i])
        count=0
        for j in lis_t:
            if lis_t[i]==j:
                count+=1
        print(lis_t[i],"-->",count)
        if count>highest:
            highest=count
            high_freq=lis_t[i]
        if count<lowest :
            lowest=count
            # if count==lowest:  
            least_freq=lis_t[i]
else:
    print(" No valis_tid data found")

print(f"Most Frequent: {high_freq}")
print(f"lis_teast Frequent: {least_freq}")
