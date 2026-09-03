
# 5.

# =========================================
# WORD LENGTH GROUPING
# ====================

# A content management system stores article tags.

# tags = ["python","java","api","react","html","css"]

# Write a program to:

# * Group words according to their length.
# * Store result in dictionary.

# Sample Output:
# {
# 3:['api','css'],
# 4:['java','html'],
# 5:['react'],
# 6:['python']
# }

# ---
print("===========================")
print("  WORD LENGTH GROUPING")
print("============================")
tags = {}
t = [tag for tag in input("enter the lang names:").split() ]

for x in t:
    if len(x) in tags:
        tags[len(x)].append(x)
    else:
        tags[len(x)] = [x]

for k,v in tags.items():
    # print({k:v})
    print(k, ":", v)