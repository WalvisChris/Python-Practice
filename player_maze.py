"""
Unfinished
"""

import os
import random

def show():
    for y in maze:
        line = ""
        for x in y:
            line += str(x)
        print(line)

WIDTH = 15
HEIGHT = 15
maze = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]

for y in range(HEIGHT):
    for x in range(WIDTH):
        if x == 0 or x == WIDTH-1 or y == 0 or y == HEIGHT-1:  
            maze[y][x] = "███"
        else:
            maze[y][x] = random.choice(['███', '   '])

os.system('cls')
show()
