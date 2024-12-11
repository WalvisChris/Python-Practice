"""
spelling bee
"""

import os
import pyttsx3
import random

engine = pyttsx3.init()

wordlist = []
wordlist.append(["khabib nurmagomadov", "a russian MMA fighter", "khabib nurmagomadov is the best wrestler ever"])
wordlist.append(["Butterfly", "A fly made of butter", "A saw a butterfly flying outside"])

os.system('cls')

previous = ""
running = True
while running:
    q = wordlist[random.randint(0, len(wordlist)-1)]
    if q[0] == previous:
        continue
    previous = q[0]
    engine.say(f"Spell {q[0]}")
    engine.runAndWait()
    user = str(input("> ")).lower()
    if user == str(q[0]).lower():
        engine.say(f"Good job! You successfully spelled {q[0]}")
        engine.runAndWait()
        continue
    if user == 'definition':
        engine.say(f"{q[0]}, {q[1]}")
        engine.runAndWait()
        continue
    if user == 'sentence':
        engine.say(f"{q[0]} in a sentence {q[2]}")
        engine.runAndWait()
        continue
    engine.say(f"Wrong!")
    engine.runAndWait()