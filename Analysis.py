from Board import Board
from math import floor
from time import sleep

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
    b1.output_potential_numbers()

    b1.scrape_valid()
    b1.output_grid()

    b1.flush()

    print()

    if not cont:
        break