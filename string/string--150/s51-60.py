# 51Extract only digits. S = "a1b2c3" "123"
# s= input("enter the string :")
# res=""
# for i in range(len(s)):
#     if s[i].isdigit() :
#         res+=s[i]
# print(res)

# ----------------------->
# 52Remove all special characters. S = "a!@b#c" "abc"
# s= input("enter the string :")
# res=""
# for i in range(len(s)):
#     if s[i].isdigit() or s[i].isalpha() or s[i]==" " :
#         res+=s[i]
# print(res)
# ----------------------->
# 53Remove punctuation. S = "Hello, world!" "Hello world"
# s= input("enter the string :")
# res=""
# for ch in s:
#     if ch.isalnum() or ch==" ":
#         res+=ch 
# print(res)


# ----------------------->
# 54Replace duplicate chars with '$'. S = "hello" "he$lo"
# s = input("enter the string:  ")
# res=""
# for i in range(len(s)):
#     if s[i] in s[:i]: # if we dont do this it will still run
#         res+=s[i] 
#     elif s[i] in s[i+1:]:#checking after i to end 
#         res+="$"
#     else:
#         res+=s[i]
# print(res)

# ----------------------->😢
# 55Reverse only vowels. S = "hello" "holle"
# st = input("enter the string:  ").lower()
# s= list(st)# s is list here
# vowel = []

# res=[]
# i = 0
# while i<len(s):
#     if s[i] in "aeiou" :
#         #taking in reverse
#         vowel.append(s[i])
#     i+=1

# v = len(vowel)-1
# for i in range(len(s)):
#     if s[i] not in "aeiou" :
#         res.append(s[i])
#     else:
#         curr = vowel[v]
#         v-=1
#         res.append(curr)
# print("".join(res))
# ----------------------->
# 56Reverse only consonants. S = "apple" "eplpa"😢
# st = input("enter the string:  ").lower()
# s= list(st)# s is list here
# consonent = []

# res=[]
# i = 0
# while i<len(s):
#     if s[i] not in "aeiou" :
#         #taking in reverse
#         consonent.append(s[i])
#     i+=1

# c = len(consonent)-1
# for i in range(len(s)):
#     if s[i] in "aeiou" :
#         res.append(s[i])
#     else:
#         curr = consonent[c]
#         c-=1
#         res.append(curr)
# print("".join(res))
# ----------------------->
# 57Merge two strings alternatively. S1 = "ABC", S2 = "def" "AdBeCf"
# s1= input("enter the string:")
# s2 = input("enter next string:")
# res=""
# f=0
# sec=0
# for i in range(len(s1)+len(s2)):
#     if  f<len(s1):
#         if i%2==0:
#            res+=s1[f]
#            f+=1
#         elif sec<len(s2): 
#             res+=s2[sec]
#             sec+=1
#         else:
#             res+=s1[f]
#             f+=1
#     elif sec<len(s2):
#         res+=s2[sec]
#         sec+=1

# print(res)

# ----------------------->
# 58Rotate characters left by 2 positions. S = "abcde" "cdeab"
# s = input("enter the string to left rotate:")
# st = list(s)
# n=len(st)
# k =2
# for i in range(k):
#     hold = st[0]
#     for j in range(n):
#         if j==n-1:
#             st[j] = hold
#         else:
#           st[j]=st[j+1]    
        
# print("".join(st))

# ----------------------->
# 59Rotate characters right by 3 positions. S = "abcde" "cdeab"
# s = input("enter the string to right rotate:")
# s1 = list(s)
# n=len(s1)
# k =3
# for i in range(k):
#     hold = s1[n-1]
#     for j in range(n-1,-1,-1):    
#         if j==0:
#            s1[j]=hold
#         else:
#             s1[j]=s1[j-1]
# print("".join(s1))
# ----------------------->  
# 60Append two strings but remove adjacent duplicates. S1="miss", S2="issippi" "misisipi"
s1 = input("enter the string:")
s2 = input("enet the string: ")

new=[]
ls1 = list(s1)
ls2 = list(s2)
ls3 = ls1+ls2
n= len(ls3)
new=[]
for i in range(n-1):
    if ls3[i]!=ls3[i+1]:
        new.append(ls3[i])
new.append(ls3[n-1])    
print("".join(new))
