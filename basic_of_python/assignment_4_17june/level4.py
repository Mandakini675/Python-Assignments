"""------------------------
Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km
-------------------------"""
speed = int(input("enter your speed km/hr"))
time = int(input("enter time taken in hours :"))
time2 = int(input("enter time taken in minutes :"))
total_time = (time2/60)+time

dis = speed*total_time
print("Total Time = ",total_time,"hours")
print("Distance = ",dis)