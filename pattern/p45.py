n=int(input("enter numbr: "))
i = n
while i>0:
    ch=65
    j=1
    while j<i:
        print(" ",end="")
        j+=1
    k=1
    while k<=n-i+1:
        print(chr(ch),end="")
        ch+=1
        k+=1
    i-=1
    print()

# enter numbr: 5
#     A
#    AB
#   ABC
#  ABCD
# ABCDE
# n=int(input("enter numbr: "))
# i = n

# while i>0:
#     j=1
#     while j<=i:
#         if i==n or j==1 or i==j :
#           print(i,end="")
#         else:
#             print(" ",end="")
#         j+=1
#     i-=1
#     print()

# # 55555
# # 4__4
# # 3_3
# # 22
# # 1
