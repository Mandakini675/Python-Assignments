
s=input("enter string:")
ans=""
for i in range(len(s)):
    st=0
    en=i
    for j in range(i,len(s)):

        print(s[i:j])
        

        st+=1
        en+=1
print(ans)