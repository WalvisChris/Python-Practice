"""
Calorie maitenance calculator
"""

import os

os.system('cls')
sex = str(input("sex (m/f): "))
weight = int(input("weight (kg): "))
height = int(input("height (cm): "))
age = int(input("age: "))
activity = int(input("activity (1-5): "))
if sex == 'm':
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
if sex == 'f':
    bmr = 10 * weight + 6.25 * height - 5 * age - 161
multiplier = [1.2, 1.375, 1.55, 1.725, 1.9]
calories = bmr * multiplier[activity-1]
print("Maintenance calories:", calories)