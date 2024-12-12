"""
Solves a sudoku. I did use ChatGPT to go back a iteration
"""

import os

sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# for colors
initial_sudoku = [row[:] for row in sudoku]

def is_valid(horizontal: int, vertical: int, value: int) -> bool:
    
    # check row
    row = sudoku[vertical]
    if value in row:
        return False

    # check column
    column = [sudoku[x][horizontal] for x in range(9)]
    if value in column:
        return False

    # check cell
    b = horizontal // 3
    c = vertical // 3
    cell = [d[b*3:b*3+3] for d in sudoku[c*3:c*3+3]]
    if any(value in row for row in cell):
        return False

    return True

def try_solve():
    empty_cells = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
    index = 0

    while index < len(empty_cells):
        i, j = empty_cells[index]
        found = False

        start_value = sudoku[i][j] + 1 if sudoku[i][j] != 0 else 1
        for value in range(start_value, 10):
            if is_valid(j, i, value):
                sudoku[i][j] = value
                found = True
                break

        if not found:
            sudoku[i][j] = 0
            index -= 1
            if index < 0:
                return False
        else:
            index += 1

        show()

    return True

def show():
    WHITE = "\033[97m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    image = ""
    for i, row in enumerate(sudoku):
        for j, value in enumerate(row):
            if initial_sudoku[i][j] != 0:
                image += WHITE + str(value) + " "
            else:
                image += YELLOW + ". " if value == 0 else YELLOW + str(value) + " "
            
            if (j + 1) % 3 == 0 and j < 8:
                image += RESET + "│ "
        image += RESET + "\n"
        
        if (i + 1) % 3 == 0 and i < 8:
            image += "──────┼───────┼──────\n"
    os.system('cls')
    print(image)


running = True
while running:
    if try_solve():
        print("Sudoku solved!")
        running = False
    else:
        print("No solution exists.")
        running = False