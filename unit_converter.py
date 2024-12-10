"""
simple unit converter
"""

import os

def handle_prompt(a, b, c):
    if a not in ['kg', 'g', 'lbs', 'cm', 'dm', 'm', 'km', 'inch', 'ft']:
        print("Invalid unit:", a)
        return
    if not isinstance(a, float):
        print("Invalid value:", b)
        return
    if c not in ['kg', 'g', 'lbs', 'cm', 'dm', 'm', 'km', 'inch', 'ft']:
        print("Invalid goal unit:", c)
        return
    
    result = 0
    # weight
    if a == 'kg':
        if c == 'g':
            result = b*1000
        elif c == 'lbs':
            result = b*2.25
    elif a == 'g':
        if c == 'kg':
            result = b/1000
        elif c == 'lbs':
            result = b/453
    elif a == 'lbs':
        if c == 'kg':
            result = b/2.25
        elif c == 'g':
            result = b*453
    # distance
    elif a == 'cm':
        if c == 'dm':
            result = b/10
        elif c == 'm':
            result = b/100
        elif c == 'km':
            result = b/100000
        elif c == 'inch':
            result = b*0.3937
        elif c == 'ft':
            result = b*0.0328
    elif a == 'dm':
        if c == 'cm':
            result = b*10
        elif c == 'm':
            result = b/10
        elif c == 'km':
            result = b/10000
        elif c == 'inch':
            result = b*3.937
        elif c == 'ft':
            result = b*0.328
    elif a == 'm':
        if c == 'cm':
            result = b*100
        elif c == 'dm':
            result = b*10
        elif c == 'km':
            result = b/1000
        elif c == 'inch':
            result = b*39.37
        elif c == 'ft':
            result = b*3.28
    elif a == 'km':
        if c == 'cm':
            result = b*100000
        elif c == 'dm':
            result = b*10000
        elif c == 'm':
            result = b*1000
        elif c == 'inch':
            result = b*39370.1
        elif c == 'ft':
            result = b*3280.84
    elif a == 'inch':
        if c == 'cm':
            result = b*2.54
        elif c == 'dm':
            result = b*0.254
        elif c == 'm':
            result = b*0.0254
        elif c == 'km':
            result = b*0.0000254
        elif c == 'ft':
            result = b/12
    elif a == 'ft':
        if c == 'cm':
            result = b*30.48
        elif c == 'dm':
            result = b*3.048
        elif c == 'm':
            result = b*0.3048
        elif c == 'km':
            result = b*0.0003048
        elif c == 'inch':
            result = b*12
    print(result, c)

os.system('cls')
user = str(input("<unit> <amount> <new_unit>: "))
prompt = user.split(" ")
if len(prompt) == 3:
    handle_prompt(prompt[0], float(prompt[1]), prompt[2])
else:
    print("Invalid prompt")