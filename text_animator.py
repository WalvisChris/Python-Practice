"""
Shows text letter for letter
"""

import os

upper = (65, 90)
lower = (97, 122)

os.system('cls')
text = str(input("> "))

output = ""
letter = ""
for char in text:
    if ord(char) in list(range(min(upper), max(upper)+1)):
        for i in range(min(upper), ord(char)+1):
            letter = chr(i)
            os.system('cls')
            print(output + letter)
    elif ord(char) in list(range(min(lower), max(lower)+1)):
        for i in range(min(lower), ord(char)+1):
            letter = chr(i)
            os.system('cls')
            print(output + letter)
    else:
        letter = char
    output += letter