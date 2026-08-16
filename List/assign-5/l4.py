
# 4.
# Find common elements in three sorted arrays.
# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
# Note: can you take care of the duplicates without using any additional Data Structure?
# Example 1:
# Input:
# n1 = 6; A = {1, 5, 10, 20, 40, 80}
# n2 = 5; B = {6, 7, 20, 80, 100}
# n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
# Output: 20 80
# Explanation: 20 and 80 are the only
# common elements in A, B and C.

n1 = int(input("how many elements you want state in A here: "))
A = [int(x) for x in input("enter the elemnts here for A :").split()]
n2 = int(input("how many elements you want state in B here: "))
B = [int(x) for x in input("enter the elemnts here for B :").split()]
n3 = int(input("how many elements you want state  in C here: "))
C = [int(x) for x in input("enter the elemnts here for C :").split()]
new = []
i =0
while i<n1:
    curr = A[i]
    for j in range(n2):
        curr2 = B[j]
        if curr == curr2:
            for k in range(n3):
                if curr2 == C[k]:
                    if curr2 not in new:
                       new.append(curr2)
                       break
    i += 1
print(new)


#TRYING TO OPTIMIZE
# n1 = int(input("how many elements you want state in A here: "))
# A = [int(x) for x in input("enter the elemnts here for A :").split()]
# n2 = int(input("how many elements you want state in B here: "))
# B = [int(x) for x in input("enter the elemnts here for B :").split()]
# n3 = int(input("how many elements you want state  in C here: "))
# C = [int(x) for x in input("enter the elemnts here for C :").split()]
# new = []
# i =0
# while i<n1:
#     curr = A[i]
#     for j in range(n2):
#       if curr<B[j]:
#         break
#       else:
#         curr2 = B[j]
#         if curr == curr2:
#             for k in range(n3):
#                 if curr<C[j]:
#                    break
#                  else:
#                 if curr2 == C[k]:
#                     new.append(curr2)
        
#     i += 1
# print(new)