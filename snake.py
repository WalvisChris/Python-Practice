"""
Unfinished
"""

import os
import random

def show():
    image = ""
    for y in game:
        for x in y:
            image += str(x)
        image += "\n"
    os.system('cls')
    print(image)

direction = 0   # 0: up, 1: right, 2: down, 3: left
length = 3
apple_position = (5, 5)

WIDTH = 15
HEIGHT = 15
game = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]

tile_index = 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        if x == 0 or x == WIDTH-1 or y == 0 or y == HEIGHT-1:  
            game[y][x] = "███"
        elif (x, y) == apple_position:
            game[y][x] = "\033[31m███\033[0m"
            tile_index += 1
        else:
            game[y][x] = "\033[32m███\033[0m" if tile_index%2==0 else "\033[92m███\033[0m"
            tile_index += 1

show()