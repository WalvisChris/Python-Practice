import os
import random

os.system('cls')
user = int(input("Amount of dices? "))
result = {}
for i in range(user):
    result[f"Dice {i}"] = random.randint(1, 6)
print(result)