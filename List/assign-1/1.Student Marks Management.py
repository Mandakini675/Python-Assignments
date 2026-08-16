'''1.Student Marks Management=====================================================================

Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3'''
l1=[]
n=int(input("enter the no of subjects: "))
for i in range(n):
    l1.append(int(input()))
count=0
largest = l1[0]
lowest = l1[0]
for i in range(len(l1)):
    largest=l1[i] if l1[i]>largest else largest
    lowest=l1[i] if l1[i]<lowest else lowest
    if l1[i]>75:
        count+=1
print(f"highest = {largest} , lowest = {lowest} , count above = {count}")