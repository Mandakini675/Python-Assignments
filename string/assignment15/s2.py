'''2.
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5'''

s = input("enter string = ")
spac = 0

for n in range(len(s)):
    if s[n]==" ":
       spac+=1
print(f" Total spaces: {spac}")