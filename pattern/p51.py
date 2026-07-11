n= int(input("enter number :"))
i=n
while i>0:
    j=n
    while j>i:
        print(".",end="")
        j-=1

    k=1
    while k<=i:
        if k==1 or i==k or i==n:
            print(k,end="")
        else:
            print("_",end="")
        k+=1
    i-=1
    print()

# enter number :5
# 12345
# .1__4
# ..1_3
# ...12
# ....1