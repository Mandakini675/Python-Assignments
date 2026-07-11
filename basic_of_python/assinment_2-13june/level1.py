"""An event management company is developing a scheduling system. One of the key tasks is converting the duration of events from total seconds (which their sensor system records) into a more human-readable format of hours, minutes, and seconds.

Write a Python program that:
- Accepts the total event duration in seconds as input.
- Calculates how many hours, minutes, and seconds it corresponds to.
- Displays the output in the format:
  Hours: x, Minutes: y, Seconds: z

Sample Input:
Total event duration in seconds: 3672

Sample Output:
Hours: 1, Minutes: 1, Seconds: 12"""


print("TO Convert sec into regular time duration")

inpsec=int(input("Enter the second"))
hrs = inpsec//(60*60)
min = (inpsec%(60*60))//60
remaining_seconds = inpsec % 3600

sec =(remaining_seconds)%60

print("Hours :",hrs,",Minutes :",min,",Seconds :",sec)