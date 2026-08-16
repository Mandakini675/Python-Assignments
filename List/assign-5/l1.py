# 1. Count Pairs with Difference K

# A company records the ages of employees.
#  Find how many pairs of employees have an age 
#  difference exactly equal to K.
# Problem Statement:
# Given an array of employee ages and an integer K
# count the number of pairs whose absolute difference is K.
# Example:

# Input:

# N = 5
# K = 2
# ages[] = {1, 5, 3, 4, 2}
# Output:
# 3
# Explanation:

# (1,3), (3,5), (2,4)
n = int(input("how many employee are there state with no .:"))
ages =[int(x) for x in input("enter the ages of all emplayee by spaces --:").split()]
k = 2
count= 0
for i in range(n):
    for j in range(i,n):
        if abs(ages[i]-ages[j])==k:
            count+=1
            print(f"( {ages[i]} , {ages[j]})")
print("count ="count)