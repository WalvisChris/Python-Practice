"""
Unfinished
"""

import os
import random
import time

class Ball:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

def show():
    image = ""
    for y in game:
        for x in y:
            image += str(x)
        image += "\n"
    os.system('cls')
    print(image)

def move():
    if ball.direction % 3 == 0:
        ball.position = (ball.position[0] - 1, ball.position[1])
    else:
        ball.position = (ball.position[0] + 1, ball.position[1])

    if ball.direction < 2:
        ball.position = (ball.position[0], ball.position[1] + 1)
    else:
        ball.position = (ball.position[0], ball.position[1] - 1)
    """
    if ball.direction == 0:
        ball.position[0] -= 1
        ball.position[1] += 1
    elif ball.direction == 1:
        ball.position[0] += 1
        ball.position[1] += 1
    elif ball.direction == 2:
        ball.position[0] += 1
        ball.position[1] -= 1
    else:
        ball.position[0] -= 1
        ball.position[1] -= 1
    """

WIDTH = 15
HEIGHT = 15

ball = Ball((5, 5), 0)
game = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]

tile_index = 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        if x == 0 or x == WIDTH-1 or y == 0 or y == HEIGHT-1 or (x, y) == ball.position:  
            game[y][x] = "██"
        else:
            game[y][x] = "  "

running = True
while running:
    show()
    move()
    time.sleep(1)