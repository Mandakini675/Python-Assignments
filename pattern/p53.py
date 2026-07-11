n= int(input("enter number :"))
i=n
while i>0:
    ch=65
    j=n
    while j>i:
        print(".",end="")
        j-=1

    k=1
    while k<=i:
        if k==1 or i==k or i==n:
            print(chr(ch),end="")
        else:
            print("_",end="")
        ch+=1
        k+=1
    i-=1
    print()