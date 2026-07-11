"""-----------------
--

Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0

---------------------"""
mb_price = int(input("enter mobile price"))
down_payment= int(input("down payment "))
interest_per = int(input("enter interest rate : "))
month = int(input("how many months: "))
remain_amount = mb_price - down_payment
interest = (interest_per/100)*remain_amount
total = interest + remain_amount
emi = total/month

print("Expected Amount = ",remain_amount)
print("Total with interest = ",total)
print("Monthly EMI = ",emi)
 

