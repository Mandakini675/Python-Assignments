 n= int(input("enter n ="))
#           * 
#         * * 
#       * * * 
#     * * * * 
#   * * * * * 

m=n
i=1
while i<=n:
    print()

    j=n
    while j>=i:
        print(" ",end=" ")
        j-=1
    en = 1
    while en<=i:
        print("*",end=" ")
        en+=1
    i+=1
    


    # ------*   n=6  j =1-6
    # -----**        j=1-5
    # ----***        j=1-4
    # ---****
    # --*****
    # -******
    