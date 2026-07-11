# 654321 i=1 j=6-1
#  65432 i=2 j=6-2 
#   6543 i=3
#    654
#     65
n= int(input("enter n ="))
i=1
while i<n:
# while i<=n:
    print()
    j=1
    while j<=i:
        print(" ",end="")
        j+=1

    k=n
    while k>=i:
        print(k,end="")
        k-=1
    i+=1
    



# i=n
# while i>=1:
#     print()
#     j=n
#     while j>=n-i+1:
#         print(j,end="")
#         # print("@",end="")
#         j-=1
#     i-=1