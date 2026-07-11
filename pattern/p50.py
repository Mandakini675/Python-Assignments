n= int(input("enter number :"))
i=n
while i>0:
    j=n
    while j>i:
        print(".",end="")
        j-=1

    k=1
    while k<=i:
        print(i,end="")
        k+=1
    i-=1
    print()

# enter number :5
# 55555
# .4444
# ..333
# ...22
# ....1