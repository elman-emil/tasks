# Minesweeper field demo (help with copilot)

import random

def create_minefield(rows, cols, mines):
    field = []

    
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        field.append(row)

    
    placed = 0
    while placed < mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)

        if field[r][c] != "*":
            field[r][c] = "*"
            placed += 1

    return field
