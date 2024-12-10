"""
prints random strings from a list
"""

import os
import random

os.system('cls')
answers = ['Yes', 'No', 'Absolutely', 'No way', 'Never', 'Definitely']
user = input("Question: ")
print(answers[random.randint(0, len(answers)-1)])