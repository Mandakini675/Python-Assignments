"""---------------------
Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75

------------------"""

total_bill = int(input("enter total bill"))
gst = int(input("enter gst %: "))
ser_charge = int(input("enter service charge : "))
no_frnd = int(input("how many friends you were: "))
 
GST = (gst/100)*total_bill
service = (ser_charge/100)*total_bill
final = GST + service + total_bill

#print(GST)
#print(service)
#print(total_bill)

print("Final bill : ",final)
print("Each person pays = ",final/no_frnd)