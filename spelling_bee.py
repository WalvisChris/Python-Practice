import os
import pyttsx3
import random

class Word:
    def __init__(self, text, definition, sentence):
        self.text = text
        self.definition = definition
        self.sentence = sentence
    
    def __str__(self):
        return self.text

engine = pyttsx3.init()

wordlist = []
wordlist.append(Word("khabib nurmagomadov", "a russian MMA fighter", "khabib nurmagomadov is the best wrestler ever"))
wordlist.append(Word("Butterfly", "A fly made of butter", "A saw a butterfly flying outside"))

os.system('cls')

previous = ""
running = True
while running:
    q = wordlist[random.randint(0, len(wordlist)-1)]
    if q.text == previous:
        continue
    previous = q.text
    engine.say(f"Spell {q.text}")
    engine.runAndWait()
    user = str(input("> ")).lower()
    if user == q.text:
        engine.say(f"Good job! You successfully spelled {q.text}")
        engine.runAndWait()
        continue
    if user == 'definition':
        engine.say(f"{q.text}, {q.definition}")
        engine.runAndWait()
        continue
    if user == 'sentence':
        engine.say(f"{q.text} in a sentence {q.sentence}")
        engine.runAndWait()
        continue
    engine.say(f"Wrong!")
    engine.runAndWait()