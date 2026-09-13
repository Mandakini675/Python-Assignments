
# 7.
# Assignment: File Compression System (String Compression)

# A file compression company wants to reduce the size of text files before storing them. One simple compression technique is to replace consecutive repeated characters with the character followed by its count.

# For example:

# AAABBCCCCD → A3B2C4D1

# As a software developer, your task is to write a recursive Python program to compress a given string.

# Task

# Write a recursive function that compresses a string by counting consecutive occurrences of each character.

# Input
# Enter a String:
# AAABBCCCCD
# Output
# Compressed String = A3B2C4D1
# Sample Input 2
# Enter a String:
# WWWWXXYYZ
# Sample Output 2
# Compressed String = W4X2Y2Z1
# Sample Input 3
# Enter a String:
# AAAAA
# Sample Output 3
# Compressed String = A5


# st = input("enter the string:")

# def reduce(string,i,count,res):
    
#     if i==len(string):
#        return res
#     if i==1:
#        res+=string[0]
#     if string[i]!=string[i-1]:
#        if res!="":
#           res += str(count)
#        res+=string[i]
#        return reduce(string,i+1,1,res)
       
#     else:
#        count+=1
#     return reduce(string,i+1,count,res)
# print("Compressed String =",reduce(st,1,1,""))




st = input("enter the string:")

def reduce_string(string,i,count,char,res):

   #  """ as first is not processed if unequal to next"""
   #  if i ==1:
   #     char = string[0]
    
    if i==len(string):
       res+=char
       res+=str(count)
       return res
    if string[i]==string[i-1]:
       char = string[i]
       count+=1
       return reduce_string(string,i+1,count,char,res)       
    else:
       res+=char
       res+=str(count)
       char = string[i]
       return reduce_string(string,i+1,1,char,res)

#CALIING FUNCTION here
print("Compressed String is =",reduce_string(st,1,1,st[0],""))
# print(reduce_string.__doc__)


# pseudo code
# FUNCTION compress(i, count, char, result)

#     IF i == length of string
#         save final character + count
#         RETURN result

#     IF current == previous
#         increase count
#         move to next character

#     ELSE
#         save previous character + count
#         start new character
#         reset count to 1
#         move to next character

#     RECURSE