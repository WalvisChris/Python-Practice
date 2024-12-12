"""
Looks for pattern
"""

import os

os.system('cls')
pattern = str(input("Pattern: "))
string = str(input("String: "))

for i in range(len(string)):
    if string[i:i+len(pattern)] == pattern:
        print(" " * 8 + " " * i + "^" * len(pattern))
        break