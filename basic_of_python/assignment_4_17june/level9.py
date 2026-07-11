"""-----------------------
---

Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0
----------------------"""
dis = int(input("enter distance km : "))
mil = int(input("enter mileage km/litre : "))
pet_price = int(input("enter petrol price : "))

used = float(dis/mil)
cost = float(used*pet_price)

print("Petrol Used = ",used,"litres")
print("Total Cost = ",cost )
