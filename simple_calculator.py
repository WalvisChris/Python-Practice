"""
bad calculator
"""

import os

os.system('cls')
formula = input("Calculator: ")
operators = ["+", "-", "/", "*"]
for operator in operators:
    op = formula.find(operator)
    if op > 0:
        middle = operator
        break
a = int(formula[:op])
b = int(formula[op+1:])
if middle == '+':
    print(a+b)
elif middle == '-':
    print(a-b)
elif middle == '/':
    print(a/b)
elif middle == '*':
    print(a*b)
else:
    print("Invalid operator")