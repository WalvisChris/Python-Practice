"""
create a quiz with preset questions
"""

import os
import random

class Question():
    def __init__(self, questionText, a, b, c, d, answer):
        self.question = questionText
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.answer = answer

    def check_answer(self, x):
        return x==self.answer
    
    def __str__(self):
        return f"{self.question}\na) {self.a}\nb) {self.b}\nc) {self.c}\nd) {self.d}"
    
quiz = []
quiz.append(Question("What's 9 + 10?", "10.9", "1", "19", "21", "c"))
quiz.append(Question("Who has the most aura?", "John Pork", "Kai Cenat", "Skibidi Toilet", "Hans", "a"))
quiz.append(Question("When is christmas?", "1 dec", "25 dec", "1 nov", "25, nov", "b"))


os.system('cls')
previous = ""
running = True
while running:
    q = quiz[random.randint(0, len(quiz)-1)]
    if q.question == previous:
        continue
    previous = q.question
    user = str(input(str(q) + "\n"))
    if user in ['exit', 'stop', 'bye']:
        print("\nThanks for playing!")
        running = False
        continue
    text = "Correct!" if q.check_answer(user) else f"Incorrect! The right answer was {q.answer}!"
    print(text, "\n")