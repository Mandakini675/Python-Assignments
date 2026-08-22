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
