"""
12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680
---------------------
"""
am= int(input("Enter bill amount: "))
if am<=1000:
    gst= am * (5/100)
elif am>1000 and am<=5000:
     gst= 1000*(5/100)+ (am-1000) * (12/100)
else:
    gst =  1000*(5/100)+ (5000) * (12/100) +(am-5000) * (18/100)
if am>3000:
   gst=gst+200

print("Final Bill Amount: ₹", am+gst)