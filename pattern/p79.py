n= int(input("enter number :"))
# s=1
# i=1
# while i<=n:
#     k=n
#     while k>=i:
#         print(" ",end="")
#         k-=1
#     j=1
#     while j<=s:
#         print("*",end="")
#         j+=1
#     s+=2
#     i+=1
#     print()
# t=1
# i=1
# while i<=n:
#     k=1
#     while k<=i:
#         print(" ",end="")
#         k+=1
#     j=1
#     while j<=n+n-t:
#         print("*",end="")
#         j+=1
#     t+=2
#     i+=1
#     print()
#this ----------- is optimized way
i=1
while i<=n:
    k=n
    while k>=i:
        print(" ",end="")
        k-=1
    j=1
    while j<=2*i-1:
        print("*",end="")
        j+=1

    i+=1
    print()

i=n-1
while i>0:
    k=n
    while k>=i:
        print(" ",end="")
        k-=1
    j=1
    while j<=2*i-1:
        print("*",end="")
        j+=1
  
    i-=1
    print()



#here one line is extra--- we need to remove it

# enter number :5
#      *
#     ***
#    *****
#   *******
#  *********
#   *******
#    *****
#     ***
#      *