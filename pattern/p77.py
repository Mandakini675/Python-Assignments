n= int(input("enter number :"))
s=1
i=1
while i<=n:
    k=1
    while k<=i:
        if k==1 or k==i:
            print(k,end="")
        else: 
            print(" ",end="")
        k+=1
    i+=1
    print()
i=n
while i>0:
    k=1
    while k<i:
        if k==1 or k==i-1:
            print(k,end="")
        else: 
            print(" ",end="")
        k+=1
    i-=1
    print()

enter number :5
1
12
1 3
1  4
1   5
1  4
1 3
12
1