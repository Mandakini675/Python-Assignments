'''3.  Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java is easy

Output: Cleaned Message: Java is easy
'''
s= input("enter message :")
ans=""
for i in range(len(s)):
    if i==0 and s[i]==" ":
        continue
    if s[i]==" " :
        if  s[i-1]==" ":
           continue
    ans+=s[i]
       
print(ans)