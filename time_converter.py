"""
Converts 12h base and 24h base times
"""

import os

os.system('cls')
time = str(input("time (09:00pm/23:00): "))
if ':' not in time:
    print("You're missing ':'")
elif time[-2:] in ['am', 'pm']:
    if time[-2:] == 'am':
        print(time[:-2])
    else:
        index = time.find(":")
        hour = int(time[:index])
        hour += 12
        print(str(hour) + time[index:-2])
else:
    index = time.find(":")
    hour = int(time[:index])
    if hour < 13:
        print(time + "am")
    else:
        hour -= 12
        print(str(hour) + time[index:] + "pm")