#!/usr/bin/env python3.7

#import time
from time import localtime, mktime, strtime

start_time = localtime()
print(f"Timer started at {timestrftime('%X', start_time)}")

# Wait for user to stop timer
input("Press 'ENTER' to stop timer")

atop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print(f"Timer stopped at {time.strftime('%X', stop_time)}")
print(f"Total time: {difference} secounds")