from Board import Board
from math import floor
from time import sleep
import copy
import pandas as pd

previous_potential_numbers = 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

df = pd.read_excel('sudoku.xlsx')

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

for i in range(9):
    for j in range(9):
        if not pd.isnull(df[j][i]):
            grid[i][j] = int(df[j][i])

potential_numbers = [
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []]
]

b1 = Board(numbers, grid, potential_numbers)

while True:
    cont = b1.scrape_potential_numbers()

    if previous_potential_numbers == b1.potential_numbers and cont:
        print("Fail!")
        exit()

    previous_potential_numbers = copy.deepcopy(b1.potential_numbers)

    b1.deep_scrape_potential()
    
    b1.scrape_valid()

    b1.flush()

    if not cont:
        break

    
b1.output_grid()