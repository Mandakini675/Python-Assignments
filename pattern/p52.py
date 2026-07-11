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
            print(i,end="")
        else:
            print("_",end="")
        k+=1
    i-=1
    print()

# enter number :5
# 55555
# .4__4
# ..3_3
# ...22
# ....1