'''
6.
AI Voice-to-Text Correction System

A company has developed an AI-based voice-to-text application for virtual meetings.

Due to microphone disturbances and speech recognition delays, some words are captured multiple times consecutively in the generated text.

Before saving the meeting transcript, the system must remove duplicate words while maintaining the original order of words.

Write a Python program to remove repeated words from a sentence.

Input:
hello hello team team meeting meeting started
Output:
hello team meeting started
'''


s=input("enter sentence=")
word=s.split()
no_rep=""
for wd in word:
   if wd not in no_rep:
       no_rep+=wd+" "
   
print(no_rep)