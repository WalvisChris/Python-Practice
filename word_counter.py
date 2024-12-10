"""
counts words
"""

import os

os.system('cls')
user = input("text: ")
words = user.split()
count = {}
for word in words:
    count[word] = words.count(word)
print(count)