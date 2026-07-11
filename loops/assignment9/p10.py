'''0.
Electricity Bill Processing System (Multi-House)

An electricity board processes bills for multiple houses in a society.

Write a program to:

- Read number of houses n
- For each house:
    - Read units consumed
    - Calculate bill using slab rates:

        First 100 units      → ₹5 per unit  
        Next 100 units      → ₹7 per unit  
        Above 200 units     → ₹10 per unit  

    - Apply conditions:
        - If bill > ₹2000 → add 10% surcharge  
        - If units < 50 → give ₹100 subsidy  

    - Print bill for each house

- After processing all houses:
    - Print total bill collected
    - Print highest bill

---

Input:
3
120
250
40

Output:
House 1 Bill = 640
House 2 Bill = 1700
House 3 Bill = 100

Total Collection = 2440
Highest Bill = 1700'''
n= int(input("enter no of houses :"))
# for i in range(1,n+1):
#     unit = int(input("enter units"))
i=1
total=0
high=0
while i<=n:
  unit = int(input("enter units = "))
  bill=0
  if unit<=100:
     bill=5*unit
  elif unit<=200:
     bill = 5*100+(unit-100)*7
  else:
    bill = 5*100 + 7*100 + (unit -200)*10

  if bill>2000:
    surcharge = 0.1*bill
    bill+=surcharge
  else:
    if unit < 50 :
        bill=bill-100
  print(f"House {i}  Bill =  {bill}")
  
  total+=bill
  high = high if high>bill else bill

  i+=1
print("~"*30)
print(f"Total Collection = {total}")
print(f"Highest Bill = {high}")
print("~"*30)