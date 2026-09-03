# ----------------------->
# 61Count total alphabets, digits, and special characters. S = "a1b!c2" Alphabets: 3, Digits: 2, Special: 1
# s = input("enter the string :")
# n = len(s)
# alp =0
# count=0
# sp=0
# for i in range(n):
#     if s[i].isalpha():
#         alp+=1
#     elif s[i].isdigit():
#         count+=1
#     else:
#         sp+=1
# print(f"Alphabets: {alp}, Digits: {count}, Special: {sp}")
#=================>
# 62Count vowels and consonants. S = "apple" Vowels: 2, Consonants: 3
# s = input("enter the string :").lower()
# vowel =0
# cons =0
# for i in range(len(s)):
#     if s[i] in "aeiou":
#         vowel+=1
#     else:
#         cons+=1
# print(f"Vowels: {vowel}, Consonants: {cons}")
#------------------------->
# 63Count frequency of each character. S = "aabcc" a: 2, b: 1, c: 2
# s = input("enter the string :")
# uniq=[]
# for ch in s :
#   if ch not in uniq:
#     uniq.append(ch)
#     cnt = s.count(ch)
#     print(f"{ch} : {cnt}")
    

#---------------------->//
# 64Count frequency of each vowel. S = "programming" o: 1, a: 1 (e, i, u: 0)
# s = input("enter the string: ").lower()
# count=0
# for ch in "aeiou":
#     if ch in s:
#         count+=1
#     print(ch ,":",count)

# print(f"")

#---------------------->
# 65Count palindromic substrings. S = "aaa" 6 (a, a, a, aa, aa, aaa)
s = input("enter the string:")
count=0
for i in range(len(s)):
    for j in range(i,len(s)):
       sub = s[i:j+1]
       if sub==sub[::-1] :
          count+=1
print(count)
#---------------------->
# 66Count number of sentences in a paragraph. P = "This. Is. Test." 3
s = input("enter the string:")
l = s.split()
print(len(l))
#-------------------->
# 67Count how many times a substring appears. S = "abab", Sub = "ab" 2
s = input("enter the string:")
sub = input('enter the substring:')
j=0
count=0
for i in range(len(s)):
    if s[i:len(sub)+j]==sub:
       count+=1
    j+=1
print(count)
#--------------------->
# 68Count the sum of digits present in a string. S = "a1b2c3" 6 (1+2+3)
s = input("enter string :")
sp = list(s)       # here characters are still in string not their data type
sum =0
for i in range(len(sp)):
    if sp[i].isdigit():
        sum+=int(sp[i])
print(sum)

#-------------------------->
# 69Count how many times 'life' appears in a string. S = "life is life" 2
s = input("enter the string:").lower()
print(s.count("life"))
#-------------------------->
# 70Compare the number of times 'the' and 'is' appear. S = "the cat is on the mat" the: 2, is: 1 (theis)
s = input("enter the string:").lower()
print("the :",s.count("the"),"is :",s.count("is"))


64,65