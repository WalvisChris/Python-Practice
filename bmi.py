import os

os.system('cls')
weight = float(input("weight (kg): "))
height = int(input("length (cm): "))
print(f"BMI: {round((weight/((height/100)**2)), 2)}")