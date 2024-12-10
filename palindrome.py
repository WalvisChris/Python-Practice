"""
checks if a word is the same spelled backwards
"""

import os

os.system('cls')
user = str(input("word: "))
print(user.lower() == user.lower()[::-1])