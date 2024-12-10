import os

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

show()