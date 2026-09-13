'''# 8. Intelligent Search Query Compressor

A search engine company wants to compress user queries.

## Rules:

* Count frequency of each character
* Display characters in sorted order
* Ignore spaces
* Case insensitive

### Input:

text
Google Search


### Output:

text
a1c1e2g2h1l1o2r1s1t1'''
s=input("enter the string:")
ans=""
unique = ""
new="".join(sorted(s))

for ch in new:
    if ch==" ":
        continue
    if ch in unique:
        continue
    unique+=ch
    count=0
    for c in new:
        if c==ch:
            count+=1
    ans+=ch+str(count)
print(ans)