"""
10. Smart Restaurant Order Processing System

A restaurant offers discounts and benefits based on order amount, customer type, and payment method.

If order amount is at least 2000, then check customer type. 
If VIP, then check payment method. If online, give free dessert and 20 percent discount;
 otherwise only free dessert. If not VIP, then check if amount is at least 5000. 
 If yes, give 15 percent discount; otherwise 10 percent discount. If order amount is less than 2000, 
 then check if it is at least 1000. If yes, then if customer is VIP, give 10 percent discount; 
 otherwise 5 percent discount. If below 1000, no offer.

Input:
Order Amount = 2500
Customer Type = VIP
Payment Method = online

Output:
Offer = Free Dessert + 20% Discount
"""
amount = int(input("Order Amount: "))
customer = input("Customer Type: ")
payment = input("Payment Method: ")

if amount >= 2000:
    if customer == "VIP":
        if payment == "online":
            offer = "Free Dessert + 20% Discount"
        else:
            offer = "Free Dessert"
    else:
        if amount >= 5000:
            offer = "15% Discount"
        else:
            offer = "10% Discount"
else:
    if amount >= 1000:
        if customer == "VIP":
            offer = "10% Discount"
        else:
            offer = "5% Discount"
    else:
        offer = "No Offer"

print("Offer =", offer)