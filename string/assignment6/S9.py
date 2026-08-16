'''enter the string: java is notnmyjava is good but javais 
enter the word:java
 output = 3'''
s=input("enter the string: ")
w = input("enter the word:")
count=0
i=0
while i<=len(s)-len(w):
    j=0
    match=1
    while j<len(w):
         if s[i+j]!=w[j]:
            match=0 
            break
         j+=1
    if match==1:
        count+=1
    i+=1
print(count)