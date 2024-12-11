"""
Unfinished
"""

import os
import random

class Tile:
    def __init__(self, position, view, connections):
        self.position = position
        self.view = view
        self.connections = connections
    
    def __str__(self):
        return self.view


def show():
    for y in maze:
        line = ""
        for x in y:
            line += str(x)
        print(line)

def get_neighbor(position, direction):
    x = position[0]
    y = position[1]

    if direction == 'n' and 0 <= y-1 < HEIGHT:
        return maze[y-1][x]
    if direction == 'e' and 0 <= x+1 < WIDTH:
        return maze[y][x+1]
    if direction == 's' and 0 <= y+1 < HEIGHT:
        return maze[y+1][x]
    if direction == 'w' and 0 <= x-1 <= WIDTH:
        return maze[y][x-1]
    return -1

styles = {
    "═╣ ": "nsw",
    " ║ ": "ns",
    "═╗ ": "sw",
    "═╝ ": "nw",
    " ╚═": "ne",
    " ╔═": "es",
    "═╩═": "new",
    "═╦═": "esw",
    " ╠═": "nes",
    "═══": "ew",
    "═╬═": "nesw"
}

WIDTH = 20
HEIGHT = 20

maze = [[None for ___ in range(WIDTH)] for ___ in range(HEIGHT)]

for y in range(HEIGHT):
    for x in range(WIDTH):
        position = (x, y)
        style = random.choice(list(styles.keys()))
        maze[y][x] = Tile(position, style, styles[style])

        # check if valid
        if x > 0:
            check = get_neighbor((x, y), 'w')
            print(f"for {maze[y][x]} checking left {check}")
        if y > 0:
            check = get_neighbor((x, y), 'n')
            print(f"for {maze[y][x]} checking above {check}")

#os.system('cls')
show()