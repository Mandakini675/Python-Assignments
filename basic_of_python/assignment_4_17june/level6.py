"""------------------------
Assignment 6: Data Storage Conversion

A user wants to convert data from GB into MB and KB.

Input:
Data = 5 GB

Expected Output:
In MB = 5120.0
In KB = 5242880.0

#1 KB (Kilobyte) = 1,024 Bytes
1 MB (Megabyte) = 1,024 KB (or 1,048,576 Bytes)
1 GB (Gigabyte) = 1,024 

---------------------"""
data = int(input("enter data in gb and convert into mb and kb : "))
mb = float(data*1024)
kb = float(mb*1024)

print("In MB = ",mb)
print("In KB = ",kb)
