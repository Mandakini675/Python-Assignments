#     1
#    10
#   101
#  1010
# 10101
n= int(input("enter n ="))
i=1
while i<=n:
    print()
    j=n
    while j>=i:
        print(" ",end="")
        j-=1
    
    o_z=1
    while o_z<=i:
        if o_z%2!=0:
            print("1",end="")
        else :
            print("0",end="")
        o_z+=1

    
    i+=1
    
