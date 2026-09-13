'''.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop
'''
s= input("enter message :")

word=""
ans=""
for i in range(len(s)):
    if i==0 and s[i]==" ":
        continue
    
    if s[i]==" " :
        ans=ans+word+" "
        word=""
    word=s[i]+word 
ans+=word
   
print("Encrypted Message=",ans)