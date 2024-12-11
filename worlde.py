import os
import random

wordlist = ['water', 'block', 'ghoul', 'satyr', 'shiny', 'great', 'minds', 'adieu', 'lolly', 'level', 'hippo']
answer = random.choice(wordlist)
guesses = ""
turn = 1

def correct(s):
    return f"\033[32m{s}\033[0m"

def present(s):
    return f"\033[93m{s}\033[0m" 

os.system('cls')
running = True
while running:
    guess = str(input(f"{turn}/6: ")).lower()
    os.system('cls')

    # validate
    if len(guess) != 5:
        continue
    
    # win
    if guess == answer:
        print(guesses + correct(guess))
        running = False
        continue

    result = ["_", "_", "_", "_", "_"]
    
    # present fix 
    count = {}
    for letter in answer:
        count[letter] = answer.count(letter)

    # correct
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            result[i] = correct(guess[i])
            count[guess[i]] -= 1

    # present
    for i, letter in enumerate(guess):
        if letter in answer and count[letter] > 0 and result[i] == "_":
            result[i] = present(letter)
            count[guess[i]] -= 1

    # absent
    for i in range(len(guess)):
        if result[i] == "_":
            result[i] = guess[i]

    # UI
    guesses += "".join(result) + "\n"
    print(guesses)

    # turns
    turn += 1
    if turn > 6:
        print("You lost. The answer was:", answer)
        running = False