'''
3.
# Assignment: Prime iber Analyzer using List (Python)

## Scenario

A coaching institute stores student lucky ibers in a Python List.
Your task is to analyze the list and identify prime ibers for a scholarship selection process.

You must iterate through every element of the list and perform prime iber analysis.

---

# Requirements

Write a Python program to:

1. Store integer values in a List
2. Iterate through all elements of the List
3. Check whether each iber is prime or not
4. Display all prime ibers
5. Count total prime ibers
6. Count total non-prime ibers
7. Find the largest prime iber from the List
8. Store all prime ibers into another List
9. Sort the prime ibers in ascending order and display them

---

# Test Case 1

## Input

[2, 3, 4, 5, 6, 7, 8]

## Expected Output

Prime ibers: 2 3 5 7
Prime Count: 4
Non-Prime Count: 3
Largest Prime iber: 7
Prime List: [2, 3, 5, 7]
Sorted Prime List: [2, 3, 5, 7]

---

# Test Case 2

## Input

[10, 11, 12, 13, 14, 15]

## Expected Output

Prime ibers: 11 13
Prime Count: 2
Non-Prime Count: 4
Largest Prime iber: 13
Prime List: [11, 13]
Sorted Prime List: [11, 13]

---

# Test Case 3

## Input

[1, 2, 17, 19, 20, 25]

## Expected Output

Prime ibers: 2 17 19
Prime Count: 3
Non-Prime Count: 3
Largest Prime iber: 19
Prime List: [2, 17, 19]
Sorted Prime List: [2, 17, 19]

---

# Test Case 4

## Input

[4, 6, 8, 9, 10]

## Expected Output

Prime ibers: None
Prime Count: 0
Non-Prime Count: 5
Largest Prime iber: Not Available
Prime List: []
Sorted Prime List: []

---
# Test Case 5

## Input
[29, 31, 37, 41]

## Expected Output
Prime ibers: 29 31 37 41
Prime Count: 4
Non-Prime Count: 0
Largest Prime iber: 41
Prime List: [29, 31, 37, 41]
Sorted Prime List: [29, 31, 37, 41]
---'''

# 1. Store integer values in a List
# 2. Iterate through all elements of the List
# 3. Check whether each iber is prime or not
# 4. Display all prime ibers
# 5. Count total prime ibers
# 6. Count total non-prime ibers
# 7. Find the largest prime iber from the List
# 8. Store all prime ibers into another List
# 9. Sort the prime ibers in ascending order and display them


import math
n=int(input("enter the no of values: "))

l1=[]
pr_l=[]
count=0
count_nonpr=0
for i in range(n):
     l1.append(int(input()))
  
largest=2
for i in range(len(l1)):
    if l1[i]>1:
        j=2
        while j<=int(math.sqrt(l1[i])):
            if l1[i]%j==0:
                count_nonpr+=1
                j+=1
                break
            j+=1
        else:
            print(l1[i],end=" ")
            pr_l.append(l1[i])
            count+=1
            largest=l1[i] if l1[i]>largest else largest
pr_l2= pr_l.copy()
pr_l.sort()

print()
print(f"Prime Count: {count}")

print(f"Non-Prime Count:{count_nonpr}")
print(f"Largest Prime number: {largest}")
print(f"Prime List: {pr_l2}")

print(f"Sorted Prime List: {pr_l}")