"""
Turns text into morse
"""

import os

morse = {
    "a": "•-",
    "b": "-•••",
    "c": "-••",
    "d": "•",
    "e": "•",
    "f": "••-•",
    "g": "--•",
    "h": "••••",
    "i": "••",
    "j": "•---",
    "k": "-•-",
    "l": "•-••",
    "m": "--",
    "n": "-•",
    "o": "---",
    "p": "•--•",
    "q": "--•-",
    "r": "•-•",
    "s": "•••",
    "t": "-",
    "u": "••-",
    "v": "•••-",
    "w": "•--",
    "x": "-••-",
    "y": "-•--",
    "z": "--••"
}

os.system('cls')
result = ""
user = str(input("> "))
for char in user:
    if char == " ":
        result += "\n"
    elif char in morse.keys():
        result += morse[char] + " "
print(result)