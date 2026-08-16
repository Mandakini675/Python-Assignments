
# 5.

# Rearrange the array in alternating positive and negative items
# Given an unsorted array Arr of N positive and negative numbers.
# Your task is to create an array of alternate positive and negative numbers
# without changing the relative order of positive and negative numbers.
# Note: Array should start with positive number.

# Example 1:
# Input:
# N = 9
# Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
# Output:
# 9 -2 4 -1 5 -5 0 -3 2
# Example 2:
# Input:
# N = 10
# Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
# Output:
# 5 -5 2 -2 4 -8 7 1 8 0

res=[]
m = int(input("enter no of elements :"))
arr = [int(x) for x in input("enter all elements ").split()]
pos = []
neg = []

for c in arr:
    if c>0:
        pos.append(c)
    else:
        neg.append(c)

p=0
n=0
for i in range(m):
    if  p < len(pos) and n < len(neg):
      # this is because we have both
       if i %2== 0:
           res.append(pos[p])          
           p+=1
       else:
          res.append(neg[n])
          n+=1
    #this is if all posive ,negfinishes and only neg or only positive left so 
    elif  p < len(pos) :
        res.append(pos[p])
        p+=1
    elif n < len(neg):
        res.append(neg[n])
        n+=1
print(res)