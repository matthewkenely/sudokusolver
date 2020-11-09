from Board import Board
from math import floor
from time import sleep

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
    cont = b1.scrape_potential()
    b1.scrape_valid()
    b1.flush()

    if not cont:
        break

b1.output_grid()