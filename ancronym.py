"""
Creates an acronym for the input
"""

import os

os.system('cls')
s = str(input("> "))
words = s.split(" ")
result = ""
for word in words:
    result += word[0].upper()
print(result)