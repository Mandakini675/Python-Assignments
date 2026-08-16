'''
# 6. AI Chat Toxic Pattern Detector
An AI moderation system wants to detect whether a sentence contains three consecutive repeating characters.
If found:
text
Spam Pattern Found
Else:
text
Clean Message

### Input:
text
heyyy broooo welcome

### Output:
text
Spam Pattern Found

'''
s= input("enter string: ")
words=s.split()
spam=False
for word in words:
# every word 
    for i in range(len(word)-2):
        if word[i]==word[i+1]==word[i+2]:
            spam=True
            break
    if spam:
        break
        
if spam:
    print("spam pattern found")    
   
else:
    print("clean messege")
            