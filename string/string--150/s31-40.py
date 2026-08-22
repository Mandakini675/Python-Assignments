# 31Remove duplicate words. S = "the cat and the dog" "the cat and dog"

# s=input("enter the string =")
# w = s.split()
# uniq=""

# for i in range(len(w)):
#   if w[i] not in uniq:
#     uniq+=" "+w[i]
    
# print(uniq)
#---------------------->

# 32Count frequency of each word. S = "apple banana apple" apple: 2, banana: 1

# s=input("enter the string =")
# w = s.split()
# uniq=[]

# for i in range(len(w)):
  
#   if w[i] not in uniq:
#     uniq.append(w[i])
#     count=0
#     for j in range(len(w)):
#         if w[i]==w[j]:
#            count+=1
#     print(w[i] ,":",count)
#------------------------------>
# 33Find the longest word. S = "find the longest word" "longest"

# s=input("enter the string =")
# w = s.split()
# uniq=[]
# long= w[0]
# for i in range(len(w)):
#     long = w[i] if len(w[i])> len(long) else long

# print(long)

#--------------------------->
# 34Find the shortest word. S = "find the shortest word" "the"
# s=input("enter the string =")
# w = s.split()
# uniq=[]
# short= w[0]
# for i in range(len(w)):
#     short = w[i] if len(w[i])< len(short) else short

# print(short)
#----------------------------->
# 35Find the first palindrome word. S = "this madam is here" "madam"
# s=input("enter the string =")
# w = s.split()
# for i in range(len(w)):
#     wd = w[i]
#     rev=""
#     for j in range(len(wd)):
#        rev = wd[j]+rev 
#     if rev == wd:
#        print(wd)
#        break
#------------------------------>
# 36Reverse order of words. S = "one two three" "three two one"
# s=input("enter the string =")
# w = s.split()
# rev=""

# for i in range(len(w)):
#     rev = w[i]+" "+rev
# print(rev)
#------------------->
# 37Reverse each word. S = "cat dog" "tac god"
# s=input("enter the string =")
# w = s.split()
# new=""
# for i in range(len(w)):
#     wd = w[i]
#     rev=""
#     for j in range(len(wd)):
#        rev = wd[j]+rev 
#     new+=rev+" "
# print(new)
#--------------------------->
# 38Reverse words without split(). S = "a b c" "c b a"
# s=input("enter the string =")

# new=""
# for i in range(len(s)):
#     new = s[i]+new
# print(new)
#----------------------------->
# 39Search all occurrences of a character. S = "banana", Char='a' 1, 3, 5 (indices)
# s=input("enter the string =")
# w = input("enter the character: ")

# for i in range(0,len(s)):
#     if s[i]==w:
#       print(i,end=",")
#----------------------------->
# 40Search all occurrences of a word. S = "a b a b", Word='b' 2, 6 (start indices)
s=input("enter the string =")
w = input("enter the character: ")

for i in range(0,len(s)):
    if s[i]==w:
      print(i,end=",")
