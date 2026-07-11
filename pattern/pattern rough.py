# n = input("enter numbers:")
# count=0
# for i in n:
#         count+=1
# print(f"count= {count}")
# n = int( input("enter numbers:"))
# count=0
# while n>0:
#         d=n%10
#         count+=1
#         n//=10
# print(f"count= {count}")

# 
# 
# n=5
# i=1
# while i<=n:
#     print()
#     j=n
#     while j>=i:
#         print(j,end="")
#         # print("@",end="")
#         j-=1

#     i+=1

# 54321
# 5432
# 543
# 54
# 5
#-------------------> 

#-------------------> 
# 1
# **
# 123
# ****
# 12345


# n=5
# i=1
# while i<=n:
#     print()
#     j=1
#     while j<=i:
#         if i%2==0:
#             print("*",end="")
#         else:
#             #print(i,end="")so previous pattren will 
#             print("j",end="") 
#         j+=1
#     i+=1

# 1
# **
# 333
# ****
# 55555
#--------------------------->
n=5
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if j%2==0:
            print("*",end="")
        else:
            print(j,end="")
        # print("@",end="")
        j+=1
    i+=1
1
1*
1*3
1*3*
1*3*5