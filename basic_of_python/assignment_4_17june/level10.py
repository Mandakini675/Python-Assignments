"""-----------------------
Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4

-------------------------"""
sec = int(input("Total seconds ="))

hrs = sec//3600
min = (sec%3600)//60
sec = (sec%3600)%60

print("Hours =",hrs)
print("Minutes = ",min)
print("Seconds = ",sec)
