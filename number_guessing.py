"""
simple number guesser
"""

import random
import os

os.system('cls')
max = int(input("Max number? "))
answer = random.randint(0, max)
guessing = True
while guessing:
    user = int(input("Guess the number: "))
    guessing = not user == answer
    text = "Higher" if user<answer else "Lower"
    print(text)
print("You won!")