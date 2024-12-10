"""
better version of zodiac teller
"""

import os
from datetime import datetime

class Zodiac:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
    
    def __str__(self):
        return self.name

os.system('cls')
user = str(input("yyyy-mm-dd: "))
user = user.split("-")
bday = datetime(int(user[0]), int(user[1]), int(user[2]))
signs = [
    Zodiac("aquarius", datetime(int(user[0]), 1, 20), datetime(int(user[0]), 2, 18)),
    Zodiac("pisces", datetime(int(user[0]), 2, 19), datetime(int(user[0]), 3, 20)),
    Zodiac("aries", datetime(int(user[0]), 3, 21), datetime(int(user[0]), 4, 19)),
    Zodiac("taurus", datetime(int(user[0]), 4, 20), datetime(int(user[0]), 5, 20)),
    Zodiac("gemini", datetime(int(user[0]), 5, 21), datetime(int(user[0]), 6, 20)),
    Zodiac("cancer", datetime(int(user[0]), 6, 21), datetime(int(user[0]), 7, 22)),
    Zodiac("leo", datetime(int(user[0]), 7, 23), datetime(int(user[0]), 8, 22)),
    Zodiac("virgo", datetime(int(user[0]), 8, 23), datetime(int(user[0]), 9, 22)),
    Zodiac("libra", datetime(int(user[0]), 9, 23), datetime(int(user[0]), 10, 22)),
    Zodiac("scorpio", datetime(int(user[0]), 10, 23), datetime(int(user[0]), 11, 21)),
    Zodiac("sagittarius", datetime(int(user[0]), 11, 22), datetime(int(user[0]), 12, 21)),
    Zodiac("capricorn", datetime(int(user[0]) - 1, 12, 22), datetime(int(user[0]), 1, 19)),
]
for zodiac in signs:
    if zodiac.start <= bday <= zodiac.end:
        print("You're a", zodiac)