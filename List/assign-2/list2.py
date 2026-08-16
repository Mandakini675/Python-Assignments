
# 2.Smart City Traffic Peak Load Analyzer
# Problem Statement
# A smart city monitors traffic density at different time intervals in a day.
# An element is called a peak traffic point if it is greater than or equal to its adjacent elements.
# You are given an array traffic[] of size N.
# Tasks:
# Find all peak elements
# Calculate the sum of all peak traffic values
# Find the product of all peak traffic values
# Return the maximum peak value
# Note:
# If only one element exists, it is the only peak.

# Test Case 1

# Input:
# traffic = [10, 50, 30, 70, 60, 90, 80]

# Output:
# Peaks = [50, 70, 90]
# Sum = 210
# Product = 315000
# Max Peak = 90

# Test Case 2

# Input:
# traffic = [100, 200, 150, 180, 170]

# Output:
# Peaks = [200, 180]
# Sum = 380
# Product = 36000
# Max Peak = 200

# Test Case 3

# Input:
# traffic = [5]

# Output:
# Peaks = [5]
# Sum = 5
# Product = 5
# Max Peak = 5

#   if i==(len(traffic)-1):
    #     peak.append(traffic[i]) 
    #   else:

n=int(input("enter no of points:"))
traffic=[]
peak=[]
for i in range(n):
    traffic.append(int(input("enter the traffic points:")))
if len(traffic)==1:
    peak.append(traffic[0])
else:
  for i in range(1,len(traffic)-1):    
    if traffic[i-1] < traffic[i] > traffic[i+1]:
       peak.append(traffic[i])

sum=0
prod=1
for i in peak:
    sum+=i
    prod*=i
    high=max(peak)
print(peak)
print("sum = ",sum)
print("product = ",prod)
print("max = ",high)