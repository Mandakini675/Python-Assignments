n= int(input("enter number :"))
s=1
i=1
while i<=n:
    k=1
    while k<=i:
        print(k,end="")
        k+=1
    i+=1
    print()
p=n
while p>0:
    k=1
    while k<p:
        print(k,end="")
        k+=1
    p-=1
    print()

# enter number :5
# 1
# 12
# 123
# 1234
# 12345
# 1234
# 123
# 12
# 1