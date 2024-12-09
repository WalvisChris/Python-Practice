import os
import random

wordlist = ["hangman", "python", "guessing", "game", "practice", "stijn"]
correct = []
sprite = ["""
       ┌─────┐  
       │     │
       │
       │
       │
    ┌──┴────────┐
    │           └─┐
    └─────────────┘
""",
"""
       ┌─────┐  
       │     │
       │     O
       │
       │
    ┌──┴────────┐
    │           └─┐
    └─────────────┘
""",
"""
       ┌─────┐  
       │     │
       │     O
       │    /
       │
    ┌──┴────────┐
    │           └─┐
    └─────────────┘
""",
"""
       ┌─────┐  
       │     │
       │     O
       │    /│
       │
    ┌──┴────────┐
    │           └─┐
    └─────────────┘
""",
"""
       ┌─────┐  
       │     │
       │     O
       │    /│\\
       │
    ┌──┴────────┐
    │           └─┐
    └─────────────┘
""",
"""
       ┌─────┐  
       │     │
       │     O
       │    /│\\
       │    / 
    ┌──┴────────┐
    │           └─┐
    └─────────────┘
""",
"""
       ┌─────┐  
       │     │
       │     O
       │    /│\\
       │    / \\
    ┌──┴────────┐
    │           └─┐
    └─────────────┘
"""]

answer = list(wordlist[random.randint(0, len(wordlist)-1)])
turn = 1
guess = ""
print(answer)
running = True
while running:
    os.system('cls')
    view = [char if char in correct else "_" for char in answer]
    print(f"{sprite[turn-1]}\nguess {turn}: {guess}\nword: {"".join(view)}")
    if '_' not in view:
        print("You won!")
        running = False
        continue
    if turn > 6:
        print("He ded. No cry. Many sad.")
        running = False
        continue
    user = str(input("> "))
    if len(user) != 1:
        guess = "Invalid length"
        continue
    if user in answer and user not in correct:
        correct.append(user)
        guess = user
        continue
    guess = user
    turn += 1
