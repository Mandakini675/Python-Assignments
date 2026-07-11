n= int(input("enter number: "))
i=0
s=1
while i<n:
   
    k=1
    while k<=n-i:
        print("*",end="")
        k+=1
    j=1
    while j<=s:
        print(" ",end="")
        j+=1
    k=1
    while k<=n-i:
        print("*",end="")
        k+=1
    s+=2
    i+=1
    print()

# enter number: 5
# ***** *****
# ****   ****
# ***     ***
# **       **
# *         *