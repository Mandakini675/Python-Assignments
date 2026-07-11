n= int(input("enter number : "))
m=n
i = 1
k=n
while i<=m:
    k=n
    if i%2!=0:
        j=1
        while j<=n:
            print(j,end="")
            j+=1
    else:
       
        while k>=1:
            print(k,end="")
            k-=1   
    n=n-1
    i+=1
    print()

# enter number : 6
# 123456
# 54321
# 1234
# 321
# 12
# 1