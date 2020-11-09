from Board import Board
from math import floor
from time import sleep
<<<<<<< HEAD
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

=======

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

grid = [
    [5, 0, 0, 0, 0, 9, 6, 0, 0],
    [4, 9, 3, 0, 0, 2, 0, 5, 0],
    [8, 0, 6, 0, 1, 0, 0, 9, 7],
    [0, 3, 2, 1, 7, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 4, 0, 0, 0],
    [0, 0, 0, 0, 2, 3, 7, 1, 0],
    [3, 4, 0, 0, 5, 0, 2, 0, 6],
    [0, 6, 0, 8, 0, 0, 5, 3, 1],
    [0, 0, 8, 2, 0, 0, 0, 0, 4]
]

>>>>>>> 30ae5fbbef4f84be40308d7ebfb3bd57a6fc8ecd
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
<<<<<<< HEAD
    cont = b1.scrape_potential_numbers()

    if previous_potential_numbers == b1.potential_numbers and cont:
        print("Fail!")
        exit()

    previous_potential_numbers = copy.deepcopy(b1.potential_numbers)

    b1.deep_scrape_potential()
    
    b1.scrape_valid()

=======
    cont = b1.scrape_potential()
    b1.scrape_valid()
>>>>>>> 30ae5fbbef4f84be40308d7ebfb3bd57a6fc8ecd
    b1.flush()

    if not cont:
        break

<<<<<<< HEAD
    
=======
>>>>>>> 30ae5fbbef4f84be40308d7ebfb3bd57a6fc8ecd
b1.output_grid()