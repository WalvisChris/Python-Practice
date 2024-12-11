"""
better better version of zodiac teller
"""

import os
from datetime import datetime

os.system('cls')
user = str(input("yyyy-mm-dd: "))
user = user.split("-")
bday = datetime(int(user[0]), int(user[1]), int(user[2]))
signs = [
    ["aquarius", datetime(int(user[0]), 1, 20), datetime(int(user[0]), 2, 18)],
    ["pisces", datetime(int(user[0]), 2, 19), datetime(int(user[0]), 3, 20)],
    ["aries", datetime(int(user[0]), 3, 21), datetime(int(user[0]), 4, 19)],
    ["taurus", datetime(int(user[0]), 4, 20), datetime(int(user[0]), 5, 20)],
    ["gemini", datetime(int(user[0]), 5, 21), datetime(int(user[0]), 6, 20)],
    ["cancer", datetime(int(user[0]), 6, 21), datetime(int(user[0]), 7, 22)],
    ["leo", datetime(int(user[0]), 7, 23), datetime(int(user[0]), 8, 22)],
    ["virgo", datetime(int(user[0]), 8, 23), datetime(int(user[0]), 9, 22)],
    ["libra", datetime(int(user[0]), 9, 23), datetime(int(user[0]), 10, 22)],
    ["scorpio", datetime(int(user[0]), 10, 23), datetime(int(user[0]), 11, 21)],
    ["sagittarius", datetime(int(user[0]), 11, 22), datetime(int(user[0]), 12, 21)],
    ["capricorn", datetime(int(user[0]), 12, 22), datetime(int(user[0]), 1, 19)],
]
for zodiac in signs:
    if zodiac[1] <= bday <= zodiac[2]:
        print("You're a", zodiac[0])