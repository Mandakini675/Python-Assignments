#----------------------------->
# 41Check if a string contains a substring (without using built-in method). S1 = "Hello", Sub="ell" TRUE
# s= input("enter the string :")
# s2 = input("enter if its a substring :")
# check =False
# for i in range(len(s)-len(s2)+1):
#     j=0
#     while j<len(s2):
#         if s[i+j]!=s2[j]:       
#            break
#         j+=1
#     else:
#         check = True
#         break
# print(check)   
#~~~~~~>   by built in   
# if s.find(s2) == -1:
#     print("False")
# else:
#     print("True")
# ----------------------->
# 42Check if two strings are equal without equals(). S1 = "abc", S2 = "abc" TRUE
# s1= input("enter the string f :")
# s2= input("enter the string s :")
# if len(s1)==len(s2):
#     for i in range(len(s1)):
#         if s1[i]!=s2[i]:
#             print("False")
#             break
#     else:
#         print("True")
# else:
#     print("False")

# ----------------------->
# 43Check if two strings are rotations of each other. S1 = "abcde", S2 = "cdeab" TRUE
# s1= input("enter the string f :")
# s2= input("enter the string s :")
# isrotated = False
# s = list(s1)
# if len(s1)==len(s2):
#   for i in range(len(s1)):
#     hold = s[-1]
#     for j in range(len(s1)-1,0,-1):
#         s[j] = s[j-1]

#     s[0]= hold
#     if "".join(s) == s2:
#        isrotated = True
#        break

# print(isrotated)
# ----------------------->
# 44Check if two strings are anagrams. S1 = "listen", S2 = "silent" TRUE
# s1= input("enter the string first :")
# s2= input("enter the string sec :")
# anagram =False
# seem = []
# if len(s1)==len(s2):
#     for i in range(len(s1)):
#         if s[i] not in seem:
#            add.append(seem)
#         continue
#         if s1.count(s1[i])!=s2.count(s1[i]):
#             break
#     else:
#         anagram = True 
# print(anagram)
# ----------------------->
# 45Check whether a string starts/ends with another string.
# S = "apple pie", Prefix = "apple", Suffix = "pie" Start: True, End: True
#~~~
# s= input("enter the string :")
# pref = input("enter the prefix :")
# suff = input("enter the suffix :")
# if s.startswith(pref) and s.endswith(suff):
#     print("True")
# else:
#     print("False")

# ----------------------->
# # 46Check if a substring appears at both the start and end. S = "abcabca", Sub="abca" TRUE
# s= input("enter the string :")
# subs = input("enter the substring :")
# if s[:len(subs)] == s[-len(subs):] ==subs:
#     print("True")
# else:
#     print("False")


# ----------------------->
# 47Check for substring using concatenation trick. S1="CDAB", S2="ABCD" True (S1 is in S2+S2)
# s1 = input("enter s1:")
# s2 = input("enter s2: ")
# print(s1 in s2+s2)
#~~here checking s2 + S2 =ABCD + ABCD  -->ABCDABCD
# ----------------------->
# 48Remove all vowels. S = "aeiou XYZ" " XYZ"
# s= input("enter the string :")
# res=""
# for i in range(len(s)):
#     if s[i] in "aeiou" or s[i] in "AEIOU":
#        continue
    #   else:
    #     res +=s[i]
# if res=="":
#     res = "no result"
    
# print(res)
# ----------------------->
# 49Replace all consonants with '*' (Example suggests replacing non-vowels). S = "apple" "ap*le" (or similar output depending on implementation)
# s= input("enter the string :")
# res=""
# for i in range(len(s)):
#     if s[i] in "aeiou"or s[i] in "AEIOU" or s[i]==" " or s[i].isdigit() or s[i] in "@#$":
#         res+=s[i]
#     else:
#         res+="*"
# print(res)

# ----------------------->
# 50Remove all digits. S = "a1b2c3" "abc"
# s= input("enter the string :")
# res=""
# for i in range(len(s)):
#     if s[i].isdigit() :
#         continue
#     else:
#         res+=s[i]
# print(res)