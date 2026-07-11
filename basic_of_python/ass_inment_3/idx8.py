"""------------------------------------------------------------------------
Assignment 8: Data Storage Converter

Write a Python program that:

Accepts value in MB.
Converts into GB.

Input:
MB = 2048

Output:
GB = 2.0
----------------------------------------------------------------------"""

MB = int(input("enter mb to convert GB "))
oneGB = 1024

GB = MB/oneGB
print("GB= ",GB)