'''1. Smart Log File Error Pattern Detector

A cybersecurity company stores server logs containing repeated system activity characters.

To detect suspicious looping behavior, the analytics team wants a Python program that finds 
the longest repeating substring present in the log file.

If multiple substrings have the same length, print the first one found.

 Input:

text
abcabcbb
Output:
text
abc


---'''

#abc a,ab,abc,b,bc,c

# valid=False
# s=input("enter string:")
# ans=""
# n=0
# sub = s[i:n]
# i=0
# for j in range(i+1,len(s)+1):
#     st=i+1
#     en=len(sub)
#     valid=False
#     for k in range(st,len(s)):
#         if s[i:j]==s[st:en]:
#             ans=s[i:j]
#             valid=True
#         st+=1
#         en+=1

#     if valid :
#        if len(ans)<=len(s[i:j]):
#             ans=s[i:j]
#     n+=1
       
s = input("Enter string: ")
ans = ""

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        current = s[i:j]
        length = j - i

        for k in range(i + 1, len(s) - length + 1):
            if current == s[k:k + length]:
                if len(current) > len(ans):
                    ans = current
                break

print(ans)
    
# print(ans)
   

