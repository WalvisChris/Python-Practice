"""
Check if number is even or odd
"""

import os

os.system('cls')
n = int(input("> "))
text = "Even" if n%2==0 else "Odd"
print(text)