# 71Print all substrings. S = "abc" "a, b, c, ab, bc, abc"
# s = input("enter the string:")
# for i in range(len(s)):
#     for j in range(i,len(s)):
#        print(s[i:j+1])

# #~~~sec approach 
# new =[]
# for i in range(len(s)):
#     for j in range(i,len(s)):
#        new.append(s[i:j+1])
# print(*new)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# 72Print all substrings of length n. S = "abc", n = 2 "ab, bc"
# s = input("enter the string:")
# n=int(input("lngth :"))
# for i in range(len(s)):
#     for j in range(i,len(s)):
#        sub = s[i:j+1]
#        if len(sub)==n:
#         print(sub)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# 73Find the longest palindromic substring. S = "babad" "bab" (or "aba")
# s = input("enter the string:")
# longpalin = ""

# for i in range(len(s)):
#     for j in range(i,len(s)):
#        sub = s[i:j+1]
#        if sub==sub[::-1] :
#           if len(sub)>len(longpalin):
#               longpalin=sub
         
# print(longpalin)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# 74Find the longest substring without repeating characters. S = "abcabcbb" "abc"
# s = input("enter the string:")
# long= ""
# longpalin=""
# for i in range(len(s)):

#     for j in range(i,len(s)):
#         sub = s[i:j+1]      
#         if len(sub)>len(longpalin):
#             longpalin = sub

#             for k in range(len(sub)):
#                 if sub.count(sub[k])>1:
#                     break
#             else:
#                 long = sub
         
# print(longpalin)
# print(long)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# 75Find the longest common prefix among strings. Strings = ["flower", "flow", "flight"] "fl"
# s = input("enter  string names :")
# w=s.split()
# pref =""
# word = w[0]

# for i in range(1,len(w[0])):
   
#     similar = word[:i]

#     for j in range(len(w)):
#         curr = w[j]
#         if similar != curr[:i]:
#             break
#     else:
#        pref=similar

# print(pref)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# 76Find the longest common suffix among strings. Strings = ["baking", "making", "taking"] "king"
# s = input("enter the strings:")
# w = s.split()
# ref = w[0]
# ch= ref[-1]
# suff =""
# for k in range(1,len(ref)+1):
#     ch = ref[-k]
#     for i in range(len(w)):
#         curr = w[i]    
#         if ch != curr[-k]:
#              break
#     else:
#         suff = ch + suff
# print(suff)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# 77Find the longest substring that appears at both ends. S = "abracadabra" "abra"

# s = input("enter the string here:")
# sub = ""
# for i in range(1,len(s)):
#     if s[:i]==s[-i:]:
#         sub = s[:i]     

# print(sub)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# 78Find the longest mirror-image substring at both ends. S = "aabccbaa" "aab"


# s = input("enter the string here:")
# sub = ""
# for i in range(1,len(s)//2+1):
#     st = s[:i]
#     end = s[-i:]
#     if st== end[::-1]:
        
#       sub = st  

# print(sub)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# 79Divide a string into n equal parts. S = "abcdef", n = 3 "ab", "cd", "ef"

# s = input("ente str:")
# n = int(input("enter n :"))
# part = len(s)//n 
# new = []

# for i in range(0,len(s),part): 
#     new.append(s[i:i+part])

# print(*new)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# 80Print list items containing all characters of a given word. List = ["apple", "plea"], Word = "pal" "apple", "plea"
s = input("enter the string here:")
s2 = s.split()
word =input("enter the word:")
listitem = []

for i in range(len(s2)):
    curr = s2[i]
    for ch in word:
        if ch  not in curr:
             break
    else:
        listitem.append(curr)
print(listitem)