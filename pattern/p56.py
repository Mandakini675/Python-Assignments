n= int(input("enter number :"))
i=1

while i<=n:
    j=1
    while j<=n-i:
        print(".",end="")
        j+=1
    k=1
    while k<=i:
        print("*",end="")
        k+=1
    i+=1
    print()
    #     *
    #    **
    #   ***
    #  ****
    # *****