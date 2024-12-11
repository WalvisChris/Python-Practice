"""
Roman converter
"""

import os

os.system('cls')
user = str(input("> "))
if user.isdigit():
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    
    roman_str = ''
    num = int(user)
    for value, numeral in roman_numerals:
        while num >= value:
            roman_str += numeral
            num -= value
    print(roman_str)
else:
    roman_numerals = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    
    total = 0
    prev_value = 0
    
    for char in reversed(user):
        value = roman_numerals[char.upper()]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    print(total)