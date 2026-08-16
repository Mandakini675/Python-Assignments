
# 4.
# Palindrome Number List Checker
# Scenario

# A system checks lucky numbers which are palindromes.

# Requirements
# Check palindrome numbers
# Store palindrome numbers in list
# Count palindrome numbers
# Find largest palindrome
# Sort palindrome list
# Test Cases

# Input:
# [121, 131, 20, 44, 55, 100]

# Output:

# Palindromes: [121, 131, 44, 55]
# Count: 4
# Largest: 131
# Sorted: [44, 55, 121, 131]

n=int(input("enter the no of values: "))
print("enter values if they are palindrome")
l1=[]
palindrome=[]
count=0
largest=0

for i in range(n):
    l1.append(int(input()))
l2=l1.copy()
for i in range(len(l1)):
    j=0
    rev=0
    while l1[i]>0:
        d=l1[i]%10
        rev=rev*10+d
        l1[i]//=10
        j+=1
    if rev==l2[i]:
       palindrome.append(rev)
       count+=1
       largest=rev if rev>largest else largest
print(f"Palindromes: {palindrome}")
print(f"Count: {count}")
print(f"Largest: {largest}")
palindrome.sort()
print(f"Sorted: {palindrome}")