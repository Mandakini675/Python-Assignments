'''
---

# 4. Cloud Storage Duplicate File Name Resolver

A cloud storage company stores uploaded filenames from users.

Sometimes multiple duplicate filenames are uploaded.

The system should:

* Keep the first occurrence unchanged
* Add (1), (2), (3)... for duplicates

### Input:

text
file file image file image data


### Output:

text
file file(1) image file(2) image(1) data

'''
s=input("enter string:")
w=s.split()
new=""

for i in range(len(w)):
    if w[i] in new:
        count=0
        for j in range(i):
            if w[i]==w[j]:
                count+=1
        new+=w[i]+f"({str(count)})"+" "
        continue
    new+=w[i]+" "
print(new)      
    