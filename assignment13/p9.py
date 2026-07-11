''' Bike Service Kilometer Checker
A bike needs service every 3000 km.
Write a program to:
- Read travelled kilometers
- Print every service checkpoint till entered km

Input:
10000

Output:
3000 6000 9000
'''
n= int(input("enter kms :"))
ser_km = 3000
every=0

for i in range(1,n//ser_km+1):
    every = every+ser_km 
    print(every,end=" ")