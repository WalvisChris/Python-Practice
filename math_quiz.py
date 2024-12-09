import os
import random

questions = {
    "1 + 1": 2,
    "9 + 10": 19,
    "69 + 69": 138
}

os.system('cls')
previous = None
score = 0
running = True
while running:
    q_key = list(questions.keys())[random.randint(0, len(questions) - 1)]
    if q_key == previous:
        continue
    previous = q_key
    user = int(input(f"{q_key} = "))
    if user in ['stop', 'exit', 'bye']:
        print("Thanks for playing!")
        running = False
        continue
    if user == questions[q_key]:
        score += 1
        continue
    print("You failed! score:", score)
    running = False
    continue