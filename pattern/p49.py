n= int(input("enter number :"))
i=n
while i>0:
    j=n
    while j>i:
        print(".",end="")
        j-=1

    k=1
    while k<=i:
        print(k,end="")
        k+=1
    i-=1
    print()


# 12345
#  1234
#   123
#    12
#     1 
