n= int(input("enter number :"))
s=1
i=1
while i<=n:
    k=n
    while k>=i:
        print(" ",end="")
        k-=1
    j=1
    while j<=s:
        if j%2!=0:
            print("*",end="")
        else:
            print("_",end="")
        j+=1
    s+=2
    i+=1
    print()
t=1
i=1
while i<=n:
    k=1
    while k<=i:
        print(" ",end="")
        k+=1
    j=1
    while j<=n+n-t:
        if j%2!=0:
            print("*",end="")
        else:
            print("_",end="")
        j+=1
    t+=2
    i+=1
    print()
#here one line is extra--- we need to remove it
# enter number :5
#      *
#     *_*
#    *_*_*
#   *_*_*_*
#  *_*_*_*_*
#  *_*_*_*_*  ----->this
#   *_*_*_*
#    *_*_*
#     *_*
#      *