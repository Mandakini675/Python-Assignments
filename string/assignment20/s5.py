'''
# 5. Social Media Hashtag Trend Window

A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.

### Input:
text
aabcbcdbca

### Output:
text
dbca
### Explanation:

dbca contains all unique characters: a,b,c,d

---'''
s=input("enter the string:")
uniq=""
for ch in s:
    if ch in uniq:
        continue
    uniq+=ch
ans=""
valid = True
j=len(uniq)

for i in range(len(s)) :
    for k in range(i+j,len(s)+1):
        valid=True
        for c in uniq:
            if c not in s[i:k]:
                valid = False
                break
            
        if valid:     
            if ans == "" or len(s[i:k]) < len(ans):
                ans = s[i:k]
            break
    
print(ans)
   