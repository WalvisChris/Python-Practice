"""
a game of rock paper scissors
"""

import os
import random

os.system('cls')
user = str(input("rock/paper/scissors: "))
user = user[:1]
choises = ['r', 'p', 's']
bot = choises[random.randint(0, len(choises)-1)]
print("bot:", bot)
if user == 'r':
    if bot == 'r':
        print("Tie!")
    elif bot == 'p':
        print("You lose.")
    else:
        print("You Win!")
elif user == 'p':
    if bot == 'r':
        print("You Win!")
    elif bot == 'p':
        print("Tie!")
    else:
        print("You lose.")
else: 
    if bot == 'r':
        print("You lose.")
    elif bot == 'p':
        print("You Win!")
    else:
        print("Tie")