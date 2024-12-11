"""
Shows multiplication table
"""

import os

os.system('cls')
n = int(input("> "))
for i in range(10):
    print(f"{i+1} x {n} = {(i+1)*n}")