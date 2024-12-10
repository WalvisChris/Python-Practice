"""
Check for anagram: words are made with the same letters
"""

import os

os.system('cls')
a = str(input("word1: "))
b = str(input("word2: "))
print(sorted(a)==sorted(b))