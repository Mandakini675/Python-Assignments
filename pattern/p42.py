# n= int(input("enter number :"))
# i = 1
# while i<=n:
#     j=n
#     while j>=i:
#         print(j,end="")
#         j-=1
#     i+=1
#     print()


# 54321
# 5432
# 543
# 54
# 5

n= int(input("enter number :"))
i = 1
while i<=n:
    j=n
    while j>i:
        print(" ",end="")
        j-=1
    
    k=1
    while k<=i:
       print(k,end="")
       k+=1
    i+=1
    print()

# enter number :5
#     1
#    12
#   123
#  1234
# 12345