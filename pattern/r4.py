n=5
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i%2==0:
            print("*",end="")
        else:
            print(i,end="") #so previous pattren will 
            # print(j,end="") 
        j+=1
    i+=1

# 1
# **
# 333
# ****
# 55555

# 1
# **
# 123
# ****
# 12345