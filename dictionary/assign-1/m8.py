
# 8.

# =========================================
# LIBRARY BOOK ISSUE TRACKER
# ==========================

# A library records issued books.

# books = [
# "Python",
# "Java",
# "Python",
# "C++",
# "Java",
# "Python"
# ]

# Write a program to:

# * Count how many times each book was issued.

# Sample Output:
# {
# 'Python':3,
# 'Java':2,
# 'C++':1
# }

# ---

print("===========================")
print("  LIBRARY BOOK ISSUE TRACKER")
print("============================")

books = input("enter books name :").split()
lib = {}

for x in books:
    if x in lib:
        lib[x]+=1
    else:
        lib[x] = 1
# print(lib)
for k,v in lib.items():
    print(k ,":",v)