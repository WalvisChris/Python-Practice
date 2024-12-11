"""
Tictactoe in the terminal (type 1-9)
"""

import os
import random

def show():
    image = ""
    for i, y in enumerate(game):
        for j, x in enumerate(y):
            if x == None:
                image += "   "
            else:
                image += f" {x} "
            if j < 2:
                image += "│"
        if i < 2:
            image += "\n───┼───┼───\n"
    image += "\n"
    os.system('cls')
    print(image)

def int_to_index(n):
    n -= 1
    y = n // 3
    x = n % 3
    return (int(x), int(y))

def bot_turn():
    empty = []
    for i, y in enumerate(game):
        for j, x in enumerate(y):
            if x is None:
                empty.append((j, i))
    index = random.choice(empty)
    game[index[1]][index[0]] = "O"

def won(s):
    # rows
    for y in game:
        if y[0] == s and y[1] == s and y[2] == s:
            return True
    # columns
    for col in range(3):
        if game[0][col] == s and game[1][col] == s and game[2][col] == s:
            return True
    # diagonals
    if game[0][0] == s and game[1][1] == s and game[2][2] == s:
        return True
    if game[0][2] == s and game[1][1] == s and game[2][0] == s:
        return True
    return False

game = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

running = True
while running:
    show()
    user = int(input("> "))
    if user > 9:
        continue
    index = int_to_index(user)
    if game[index[1]][index[0]] != None:
        continue
    game[index[1]][index[0]] = "X"
    if won("X"):
        show()
        print("You won!")
        running = False
        continue
    tie = True
    for y in game:
        for x in y:
            if x is None:
                tie = False
    if tie:
        show()
        print("Tie.")
        running = False
        continue
    bot_turn()
    if won("O"):
        show()
        print("You lost.")
        running = False
        continue