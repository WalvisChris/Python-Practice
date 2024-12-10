"""
Print fibonacci sequence for 'n'
"""

import os

os.system('cls')
n = int(input("n: "))
if n > 0:
    fibonacci = [0]
if n > 1:
    fibonacci = [0, 1]
if n > 2:
    for i in range(n-2):
        a = fibonacci[i]
        b = fibonacci[i+1]
        fibonacci.append(a+b)
print(fibonacci)