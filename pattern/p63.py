n= int(input("enter number: "))
i=1
s=1
while i<=n:
   
    j=1
    while j<=n-i:
        print(" ",end="")
        j+=1
    k=1
    while k<=s:
        if k==1 or i==n or k==s:  #😢
            print(k,end="")
        else:
             print("_",end="")
        k+=1
    s+=2
    i+=1
    print()

#     1         
#    1 3   
#   1   5  
#  1     7
# 123456789