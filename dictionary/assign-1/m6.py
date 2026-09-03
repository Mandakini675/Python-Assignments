
# 6.

# =========================================
# MOBILE APP DOWNLOAD COUNTER
# ===========================

# Downloads received from different cities:

# cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

# Write a program to:

# * Count downloads city-wise.
# * Display city with maximum downloads.

# Sample Output:
# {'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
# Most Downloads : Indore

# ---
print("===========================")
print(" MOBILE APP DOWNLOAD COUNTER")
print("============================")

cities = [city for city in input("enter the city names:").split()]
city = {}
for ct in cities:
    if ct in city:
        city[ct] +=1
    else:
        city[ct] = 1
print(city)
high = max(city.values())
for ct in city:
    if city[ct] == high:
        print(f"Most Downloads : {ct}")