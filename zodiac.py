import os
from datetime import datetime

aquarius = (datetime(2024, 1, 20), datetime(2024, 2, 18))
pisces = (datetime(2024, 2, 19), datetime(2024, 3, 20))
aries = (datetime(2024, 3, 21), datetime(2024, 4, 19))
taurus = (datetime(2024, 4, 20), datetime(2024, 5, 20))
gemini = (datetime(2024, 5, 21), datetime(2024, 6, 20))
cancer = (datetime(2024, 6, 21), datetime(2024, 7, 22))
leo = (datetime(2024, 7, 23), datetime(2024, 8, 22))
virgo = (datetime(2024, 8, 23), datetime(2024, 9, 22))
libra = (datetime(2024, 9, 23), datetime(2024, 10, 22))
scorpio = (datetime(2024, 10, 23), datetime(2024, 11, 21))
sagittarius = (datetime(2024, 11, 22), datetime(2024, 12, 21))
capricorn = (datetime(2024, 12, 22), datetime(2025, 1, 19))

os.system('cls')
user = str(input("yyyy-mm-dd: "))
user = user.split("-")
bday = datetime(int(user[0]), int(user[1]), int(user[2]))

if aquarius[0] <= bday <= aquarius[1]:
    print("You're a aquarius")
elif pisces[0] <= bday <= pisces[1]:
    print("You're a pisces")
elif aries[0] <= bday <= aries[1]:
    print("You're a aries")
elif taurus[0] <= bday <= taurus[1]:
    print("You're a taurus")
elif gemini[0] <= bday <= gemini[1]:
    print("You're a gemini")
elif cancer[0] <= bday <= cancer[1]:
    print("You're a cancer")
elif leo[0] <= bday <= leo[1]:
    print("You're a leo")
elif virgo[0] <= bday <= virgo[1]:
    print("You're  a virgo")
elif libra[0] <= bday <= libra[1]:
    print("You're a libra")
elif scorpio[0] <= bday <= scorpio[1]:
    print("You're a scorpio")
elif sagittarius[0] <= bday <= sagittarius[1]:
    print("You're a sagittarius")
else:
    print("You're a capricon")