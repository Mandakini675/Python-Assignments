n= int(input("enter number :"))
i=n
s=1
while i>0:
    
    j=n
    while j>i:
        print(".",end="")
        j-=1

    k=1
    while k<=i:
        print(s,end="")
        
        k+=1
    s+=1
    i-=1
    print()

# 11111
#  2222
#   333
#    44
#     5
