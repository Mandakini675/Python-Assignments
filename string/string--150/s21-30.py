
# ----------------------->
#   21Find the first non-repeating character. S = "aabbcde" c'

# s=input("enter the string =")
# uniq=""

# store=s[0]
# for i in range(len(s)):
#   if s[i] not in uniq:
#     uniq+=s[i]
#     count=0
#     for j in range(i,len(s)):
#        if s[i]==s[j]:
#          count+=1
#     if count==1:
#         store=s[i]
#         break
    
    
    
# print(store)

# ----------------------->😑
# 22Find the last repeating character. S = "abracadabra" r'

# s=input("enter the string =")
# uniq=""

# store=s[]
# for i in range(len(s)-1,-1,-1):
#   if s[i] not in uniq:
#     uniq+=s[i]
#     count=0
#     for j in range(i,-1,-1):
#        if s[i]==s[j]:
#          count+=1
#     if count==2:
#         store=s[i]
#         break
# print(store)
        
    
# ----------------------->
#23Print all characters that occur exactly twice. S = "aabbcdee" b', 'e'

# s=input("enter the string =")
# uniq=""

# store=""
# for i in range(len(s)):
#   if s[i] not in uniq:
#     uniq+=s[i]
#     count=0
#     for j in range(i,len(s)):
#        if s[i]==s[j]:
#          count+=1
#     if count==2:
#         store+=(s[i])
       
# print(store)
# ----------------------->
# 24Check if all characters in a string are unique. S1 = "abc", S2 = "abca" S1: True, S2: False

# s=input("enter the string =")
# s2=input("enter the string =")
# uniq=""
# uniq2=""

# for i in range(len(s)):
#   if s[i] not in uniq:
#     uniq+=s[i]
    
#   if s2[i] not in uniq2:
#     uniq2+=s2[i]
# if uniq==s:
#    st = True
# else:
#   st=False
# if uniq2==s2:
#    st2 = True
# else:
#   st2=False
# print(F"S1 = {st}")
# print(f"s2 = {st2}")
# ----------------------->
# 25Count total words in a string. S = "This is a test" 4
  #easy way 
# s= input("enter string = ")
# words = s.split()
# print(len(words))
#    #manual way
# s = input("Enter string: ")
# count = 0
# for i in range(len(s)):
#     if s[i] == " ":
#         count += 1
# if len(s) == 0:
#     print(0)
# else:
#     print(count + 1)

# ----------------------->
# 26Find the first occurrence of a word. S = "Test this test", Word = "test" 10 (index)
   #manual way
# s = input("Enter string: ")
# w= input("enter the word for search : ")
# idx=0
# for i in range(len(s)-len(w)+1):
#     matched = True

#     for j in range(len(w)):
#       if s[i+j] != w[j]:
#         matched = False
#         break

#     if matched:
#       idx = i
# print("index = ", idx)
#-------------------------------->
# 27Find the last occurrence of a word. S = "Test this test", Word = "test" 15 (index)

# s = input("Enter string: ")
# w= input("enter the word for search : ")
# idx=-1
# for i in range(len(s)-1,-1,-1):
#     matched = True

#     for j in range(len(w),0):
#       if s[i+j] != w[j]:
#         matched = False
#         break

#     if matched:
#       idx = i
#       break
# print("index = ", idx)

#---------------------------------->
# 28Count occurrences of a word. S = "word word other word", Word = "word" 3

# s = input("Enter string: ")
# w= input("enter the word for search : ")
# word = s.split()
# count=0
# for i in range(len(word)):
#     if word[i]==w:
#        count+=1

    
# print("counter = ", count)
#---------------------------------->
# 29Remove occurrences of a word. S = "a test b test c", Word = "test", Remove All "a b c"

# s = input("Enter string: ")
# w= input("enter the word for search : ")
# word = s.split()
# new=""
# for i in range(len(word)):
#     if word[i]!=w:
#        new += word[i]

    
# print("new = ", new)
#==============================>
# 30Replace a word with another word. S = "old data", Old="old", New="new" "new data"
# s = input("Enter string: ")

# old= input("enter the old data : ")
# new = input("enter new data : ")
# word = s.split()

# s2=""
# for i in range(len(word)):
#     if word[i]==old:
#        s2+= new
#     else:
#        s2 += " "+word[i]
    
# print("new = ", s2)
#------------------------->
