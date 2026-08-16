
# 5.
# Given an unsorted array arr[] of size N having both negative and positive integers.
# The task is place all negative element at the end of array without changing the order of positive element and negative element.

# Example 1:
# Input :
# N = 8
# arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
# Output :
# 1  3  2  11  6  -1  -7  -5

# Example 2:
# Input :
# N=8
# arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}
# Output :
# 7  9  10  11  -5  -3  -4  -1


n= int(input("enter the size of arr:"))
l=[]
l2=[]
valid_list=[]
for i in range(n):
    num=int(input())
    if num>0:
        l.append(num)
    else:
        l2.append(num)
new = l+l2
print(new)