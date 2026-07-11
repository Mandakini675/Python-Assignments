n= int(input("enter number: "))
i=1
s=1
ch=65
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end="")
        j+=1
    k=1
    while k<=s:
        if k==1 or i==n or k==s:  #😢
            print(chr(ch),end="")
        else:
             print("_",end="")
        k+=1
    ch+=1
    s+=2
    i+=1
    print()

# enter number: 5
#     A
#    B_B
#   C___C
#  D_____D
# EEEEEEEEE
