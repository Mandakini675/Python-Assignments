
# 2.
# Secure Password Analysis

# A cybersecurity team wants to identify pairs of 
# passwords
#  having no common characters.

# Problem Statement:

# Given N strings, count the number of pairs that do 
# not share any common character.

# Example:

# Input

# N = 4
# passwords[] = {"abc", "de", "fg", "ad"}

# Output

# 3

# Explanation

# ("abc","de")
# ("abc","fg")
# ("de","fg")

n= int(input("how many employee are there state with no .:"))
passw =[x for x in input("enter the pass of all emplayee by spaces --:").split()]

count = 0
for i in range(n):
    for j in range(i,n):
        if j ==0:
            continue
        first = passw[i]
        last = passw[j]
        #loop to compare each pair
        different = True
        for l in range(len(first)):
            for m in range(len(last)):
                if first[l]==last[m]:
                   different = False
                   break
            if different!= True:
                break
        else:
            print(f"( {passw[i]} , {passw[j]})")
            count+=1
print("count =",count)