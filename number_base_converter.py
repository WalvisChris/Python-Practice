"""
Converts base units
"""

import os

os.system('cls')
n = str(input("n: "))
if n[:2] == "0b":
    print(f"Decimal: {int(n, 2)}\nHexadecimal: {hex(int(n, 2))}")
elif n[:2] == "0x":
    print(f"Decimal: {int(n, 16)}\nBinary: {bin(int(n, 16))}")
else:
    print(f"Binary: {bin(int(n))}\nHexadecimal: {hex(int(n))}")