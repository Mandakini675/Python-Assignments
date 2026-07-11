# n=5
# i=1
# while i<=n:
#     print()
#     j=1
#     while j<=i:
#         if i%2==0:
#             print("*",end="")
#         else:
#             #print(i,end="")
#             print(j,end="") #so previous pattren will 
#         j+=1
#     i+=1

# n=5
# i=1
# k=1
# while i<=n:
#     print()
#     j=1
#     while j<=i:
#         print(k,end=" ")
#         k+=1
#         j+=1
#     i+=1

n=6
i=1

while i<=n:
    print()
    inc=1
    while inc<=i:
        #print(inc,end=" ")
        print(" ",end=" ")
        inc+=1
    s=1
    while s<=(n-i)*2:
        print("*",end=" ")
        s+=1
    dec =i
    while dec>=1:
       #print(dec,end=" ")
        print(" ",end=" ")
        dec-=1 
    i+=1

# 1 _ _ _ _ _ _ _ _ _ _ 1 
# 1 2 _ _ _ _ _ _ _ _ 2 1 
# 1 2 3 _ _ _ _ _ _ 3 2 1 
# 1 2 3 4 _ _ _ _ 4 3 2 1 
# 1 2 3 4 5 _ _ 5 4 3 2 1 
# 1 2 3 4 5 6 6 5 4 3 2 1 


#  * * * * * * * * * *   
#     * * * * * * * *     
#       * * * * * *       
#         * * * *         
#           * *     