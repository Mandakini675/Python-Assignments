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
