'''
7. Remove Duplicate Words from a String

Voice Assistant Noise Correction System

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple times.

The company wants a Python program that removes duplicate words while maintaining the original order.

``
hello hello how are are you


Output:


hello how are you'''

s=input("enter sentence=")
word=s.split()
no_rep=""
for wd in word:
 
   if wd not in no_rep:
       no_rep+=wd+" "
   
print(no_rep)