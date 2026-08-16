# 1Find the length of a string. S = "programming" 11
# s=input("enter the string:")
# length=len(s)
# print(length)
# ----------------------->
#  2Copy one string to another. S1 = "source" S2 becomes "source" 
# s=input("enter the string:")
# s2=s
# print("s1=",s)
# print("s2=",s2)
# ----------------------->
#  3Concatenate two strings. S1 = "Hello", S2 = "World" "HelloWorld" 
# s=input("enter the string:")
# s2=input("enter second string:")
# s3=s+s2
# print(s3)
# ----------------------->
#  4Compare two strings (case-sensitive). S1 = "Test", S2 = "test" Not Equal (or non-zero value) 
# s=input("enter the string:")
# s2=input("enter second string:")
# if s==s2:
#    print("equal")
# else:
#     print("not equal")
# ----------------------->
# 5Compare two strings ignoring case. S1 = "Test", S2 = "test" Equal (or 0)
# s=input("enter the string:").lower()
# s2=input("enter second string:").lower()
# if s==s2:
#    print("equal")
# else:
#     print("not equal")
# ----------------------->
# 6Convert a string to uppercase. S = "hello" "HELLO" 
# s=input("enter the string:")
# str1=s.upper()
# print(str1)

# ----------------------->
# 7Convert a string to lowercase. S = "HELLO" "hello"
# s=input("enter the string:")
# str1=s.lower()
# print(str1)

# ----------------------->
# 8Toggle the case of each character. S = "MiXED" "mIxeD" 
# s=input("enter the string:")
# s2=""
# for i in range(len(s)) :
#     if s[i].islower():
#         con= s[i].upper()
#         s2+=con
#     else:
#         con= s[i].lower()
#         s2+=con  
# print(s2)
# 
# ----------------------->
# 9Check whether a string is empty. S1 = "", S2 = "A" S1: True, S2: False 
# s=input("enter the string:")
# s2=""
# if len(s)<1:
#     print("True")
# else:
#     print("False")
# ----------------------->
# 10Trim leading, trailing, or extra spaces. S = "  hello  world  " "hello world" 
# s=input("enter the string:")
# s2=""
# for i in range(len(s)):
#     if i==0 and s[i]==" ":
#         continue
#     if s[i]==" ":
#         if s[i-1]==" ":
#             continue
#     s2+=s[i]
# print(s2)

# ----------------------->
# 11Get the character at a given index. S = "Python", Index = 2 t'
# s=input("enter the string:")
# idx=int(input("enter the index to access the char="))
# print(s[idx])
    
# ----------------------->
#  12Get the Unicode code point of a character at index. S = "A", Index = 0 65 
# s=input("enter the character =")
# idx=int(input("enter the index:"))
# print(ord(s[idx]))
# ----------------------->
#  13Get the Unicode code point before index. S = "Hello", Index = 1 72 (Unicode for 'H') 
# s=input("enter the character =")
# idx=int(input("enter the index:"))
# print(ord(s[idx-1]))

# ----------------------->
# 14Find the first occurrence of a character. S = "banana", Char = 'a' 1 (index) 
# s=input("enter the character =")
# ch=input("enter the index:")
# for i in range(len(s)):
#     if s[i]==ch:
#         print(i)
#         break


# ----------------------->😑
# 15Find the last occurrence of a character. S = "banana", Char = 'a' 5 (index)
# s=input("enter the string =")
# ch=input("enter the last occ of this character:")

# for i in range(len(s)-1,0,-1):
#     if s[i]==ch:
#         print(i)
#         break

# ----------------------->
#  16Count total occurrences of a character. S = "programming", Char = 'g' 2 
# s=input("enter string:")
# ch=input("enter character: ")
# count=0
# i=0
# while i<len(s):
#     if s[i]==ch:
#         count+=1
#     i+=1
# print(count)
# ----------------------->
#  17Remove occurrences of a character. S = "banana", Char = 'a', Remove All "bnn" 
# s=input("enter string:")
# ch=input("enter character: ")
# news=""
# i=0
# while i<len(s):
#     if s[i]!=ch:
#        news+=s[i]
#     i+=1
# print(news)

# ----------------------->
#  18Replace occurrences of a character. S = "apple", Old='p', New='x' "axxle" 

# s=input("enter the string =")
# old=input("enter the old character:")
# new=input("enter the new char to replace:")
# s2=""
# for i in range(len(s)):
#     if s[i]==old:
#         s2+=new
#     else:
#         s2+=s[i]
# print(s2)


# ----------------------->
#  19Find the highest frequency character. S = "abracadabra" a'

# s=input("enter the string =")
# uniq=""
# freq=0
# store=s[0]
# for i in range(len(s)):
#   if s[i] not in uniq:
#     uniq+=s[i]
#     count=0
#     for j in range(i,len(s)):
#        if s[i]==s[j]:
#          count+=1
#     if count>freq:
#        freq=count
#        store=s[i]
    
# print(store)


# ----------------------->
#   20Find the lowest frequency character. S = "aabbcde" c', 'd', 'e' (any one or all) 

s=input("enter the string =")
uniq=""
freq= float('inf')
store=s[0]
for i in range(len(s)):
  if s[i] not in uniq:
    uniq+=s[i]
    count=0
    for j in range(i,len(s)):
       if s[i]==s[j]:
         count+=1
    if count<freq:
       freq=count
    else: 
        if freq==count:
          store+=s[i]
          continue
    store=s[i]
    
print(store)
