"""
generates random outfit from list of clothes
"""

import os
import random

hat = [None, 'cap', 'bucket']
face = [None, 'glasses', 'sunglasses', 'scarf']
torso = [None, 'shirt', 'sweater', 'blouse', 'tanktop']
pants = ['underwear', 'diaper', 'trousers']
feet = [None, 'shoes', 'sandels', 'socks']

os.system('cls')
print(f"""
     0    => {random.choice(hat)}, {random.choice(face)}
    /|\\   => {random.choice(torso)}
    / \\   => {random.choice(pants)}, {random.choice(feet)}
""")