import os

os.system('cls')
user = str(input("sentence: "))
vowels = 0
for char in user:
    if char in 'aeiou':
        vowels += 1
print(vowels)