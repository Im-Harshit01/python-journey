#This is a simple countdown timer that takes input from the user for the duration in seconds and counts down to zero, displaying the time in hours, minutes, and seconds format.

import time

duration = int(input("Enter the time : "))

for x in range(duration, -1, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end="")
    if x > 0:
        time.sleep(1)

print("\nTime's over!")
