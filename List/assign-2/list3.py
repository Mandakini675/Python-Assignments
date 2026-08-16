
# 3.Industrial Sensor Peak Energy Monitoring System
# Problem Statement
# A factory machine records energy consumption at regular intervals.
# A peak is defined as a value greater than or equal to its neighbors.
# Tasks:

# Find all peak energy values
# Compute sum of squares of peak values
# Compute average of peak values
# Return difference between max peak and min peak
# If no peaks, return -1
# Test Case 1

# Input:
# energy = [20, 40, 30, 60, 50]

# Output:
# Peaks = [40, 60]
# Sum of squares = 5200
# Average = 50
# Difference = 20

# Test Case 2

# Input:
# energy = [10, 20, 15, 25, 20, 30]

# Output:
# Peaks = [20, 25, 30]
# Sum of squares = 1525
# Average = 25
# Difference = 10

# Test Case 3

# Input:
# energy = [5]

# Output:
# Peaks = [5]
# Sum of squares = 25
# Average = 5
# Difference = 0


n=int(input("enter no of points:"))
energy=[]
peak=[]
#taking input
for i in range(n):
    energy.append(int(input("enter the energy points:")))
#performing 
if len(energy)==1:
    peak.append(energy[0])
else:
  for i in range(1,len(energy)):     
    if i==(len(energy)-1):
      if energy[i-1] < energy[i]:
        peak.append(energy[i]) 
    else:
      if energy[i-1] < energy[i] > energy[i+1]:
         peak.append(energy[i])
#print the other solutions
sum=0
s=0
for i in peak:
    sum+=i**2
    s+=i
av=s//(len(peak))  
high=max(peak)
low=min(peak)
diff = high-low
print("peaks = ",peak)
print("sum of squares = ",sum)
print("average = ",av)
print("Difference = ",diff)
