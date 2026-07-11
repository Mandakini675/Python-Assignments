# n=int(input("enter numbr: "))
# i = n

# while i>0:
#     k=n
#     while 
#     j=1
#     while j<=i:
#         if i==n or j==1 or i==j :
#           print(j,end="")
#         else:
#             print(" ",end="")
#         j+=1
#     i-=1
#     print()
# 12345
#  1__4
#   1_3
#    12
#     1


n=int(input("enter numbr: "))
i = n
while i>0:
    j=1
    while j<i:
        print(" ",end="")
        j+=1
    k=1
    while k<=n-i+1:
        print(i,end="")
        k+=1
    i-=1
    print()

# enter numbr: 5
#     5
#    44
#   333
#  2222
# 11111