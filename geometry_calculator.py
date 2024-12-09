import os
from math import pi

os.system('cls')
shape = str(input("(circle/rectangle/sphere): "))
if shape == 'circle':
    radius = float(input("radius: "))
    print(f"Area of the {shape}: {round(pi*(radius**2), 2)}")
elif shape == 'rectangle':
    width = float(input("width: "))
    length = float(input("length: "))
    print(f"Area of the {shape}: {round(width*length, 2)}")
elif shape == 'sphere':
    radius = float(input("radius: "))
    print(f"Area of the {shape}: {round(4*pi*(radius**2), 2)}")
else:
    print(f"Uknown shape: {shape}")