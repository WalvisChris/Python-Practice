"""
Adds up all digits
"""

import os

os.system('cls')
n = str(input("n: "))
n_list = [int(x) for x in n]
print(sum(n_list))