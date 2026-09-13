
# 3.

# =========================================
# WEBSITE PAGE VISIT TRACKER
# ==========================

# A website records page visits.

# pages = ["Home","About","Home","Contact","Home","About"]

# Write a program to:

# * Count visits of each page using a dictionary.
# * Display page name and visit count.

# Sample Output:
# Home visited 3 times
# About visited 2 times
# Contact visited 1 time

# ---
print("===========================")
print(" WEBSITE PAGE VISIT TRACKER")
print("============================")

pages = [page for page in input("enter the pages by giving space:").split()]
d = {}
for vis in pages:
    if vis in d:
        # d[vis] +=1  #---- it gives value of key- d[vis]
        d[vis] = d[vis]+1
    else:
        d[vis] = 1
print(d)

for k,v in d.items():
    print(f"{k} visited {v}")