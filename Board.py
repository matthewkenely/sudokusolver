from random import randint
<<<<<<< HEAD
from math import ceil
=======
from math import ceil, floor
>>>>>>> 30ae5fbbef4f84be40308d7ebfb3bd57a6fc8ecd

class Board:
    def __init__(self, numbers, grid, potential_numbers):
        self.numbers = numbers
        self.grid = grid
        self.potential_numbers = potential_numbers

    def output_grid(self):
        for i in range(9):
            for j in range(9):
                print(self.grid[i][j], end=' ')
            print()
    
    def output_potential_numbers(self):
        for i in range(9):
            for j in range(9):
                print(self.potential_numbers[i][j], end=' ')
            print()
    
<<<<<<< HEAD
    def scrape_potential_numbers(self):
=======
    def scrape_potential(self):
>>>>>>> 30ae5fbbef4f84be40308d7ebfb3bd57a6fc8ecd
        appended = False

        for row in range(9):
            for column in range(9):
<<<<<<< HEAD
                quartile = (row // 3, column // 3)
=======
                quartile = (floor(row / 3), floor(column / 3))
>>>>>>> 30ae5fbbef4f84be40308d7ebfb3bd57a6fc8ecd

                if self.grid[row][column] == 0:
                    for num in self.numbers: 
                        potential = True

                        for i in range(9):
                            if self.grid[i][column] == num:
                                potential = False

                            if self.grid[row][i] == num:
                                potential = False

                        # Quartiles

                        if quartile == (0, 0):
                            for i in range(0, 3):
                                for j in range(0, 3):
                                    if self.grid[i][j] == num:
                                        potential = False

                        if quartile == (1, 0):
                            for i in range(3, 6):
                                for j in range(0, 3):
                                    if self.grid[i][j] == num:
                                        potential = False

                        if quartile == (2, 0):
                            for i in range(6, 9):
                                for j in range(0, 3):
                                    if self.grid[i][j] == num:
                                        potential = False

                        if quartile == (0, 1):
                            for i in range(0, 3):
                                for j in range(3, 6):
                                    if self.grid[i][j] == num:
                                        potential = False

                        if quartile == (1, 1):
                            for i in range(3, 6):
                                for j in range(3, 6):
                                    if self.grid[i][j] == num:
                                        potential = False

                        if quartile == (2, 1):
                            for i in range(6, 9):
                                for j in range(3, 6):
                                    if self.grid[i][j] == num:
                                        potential = False

                        if quartile == (0, 2):
                            for i in range(0, 3):
                                for j in range(6, 9):
                                    if self.grid[i][j] == num:
                                        potential = False

                        if quartile == (1, 2):
                            for i in range(3, 6):
                                for j in range(6, 9):
                                    if self.grid[i][j] == num:
                                        potential = False

                        if quartile == (2, 2):
                            for i in range(6, 9):
                                for j in range(6, 9):
                                    if self.grid[i][j] == num:
                                        potential = False
                        
                        if potential:
                            self.potential_numbers[row][column].append(num)
                            appended = True

        return appended
    
    def scrape_valid(self):
<<<<<<< HEAD

=======
>>>>>>> 30ae5fbbef4f84be40308d7ebfb3bd57a6fc8ecd
        for row in range(9):
            for column in range(9):
                if len(self.potential_numbers[row][column]) == 1:
                    self.grid[row][column] = self.potential_numbers[row][column][0]

<<<<<<< HEAD
    def deep_scrape_potential(self):
        for row in range(9):
            for column in range(9):
                quartile = (row // 3, column // 3)

                if len(self.potential_numbers[row][column]) > 1:
                    for num in self.numbers:
                        if num in self.potential_numbers[row][column]:
                            num_count = 0

                            # Quartiles

                            if quartile == (0, 0):
                                for i in range(0, 3):
                                    for j in range(0, 3):
                                        for k in self.potential_numbers[i][j]:
                                            if k == num:
                                                num_count += 1

                            if quartile == (1, 0):
                                for i in range(3, 6):
                                    for j in range(0, 3):
                                        for k in self.potential_numbers[i][j]:
                                            if k == num:
                                                num_count += 1

                            if quartile == (2, 0):
                                for i in range(6, 9):
                                    for j in range(0, 3):
                                        for k in self.potential_numbers[i][j]:
                                            if k == num:
                                                num_count += 1

                            if quartile == (0, 1):
                                for i in range(0, 3):
                                    for j in range(3, 6):
                                        for k in self.potential_numbers[i][j]:
                                            if k == num:
                                                num_count += 1

                            if quartile == (1, 1):
                                for i in range(3, 6):
                                    for j in range(3, 6):
                                        for k in self.potential_numbers[i][j]:
                                            if k == num:
                                                num_count += 1

                            if quartile == (2, 1):
                                for i in range(6, 9):
                                    for j in range(3, 6):
                                        for k in self.potential_numbers[i][j]:
                                            if k == num:
                                                num_count += 1

                            if quartile == (0, 2):
                                for i in range(0, 3):
                                    for j in range(6, 9):
                                        for k in self.potential_numbers[i][j]:
                                            if k == num:
                                                num_count += 1

                            if quartile == (1, 2):
                                for i in range(3, 6):
                                    for j in range(6, 9):
                                        for k in self.potential_numbers[i][j]:
                                            if k == num:
                                                num_count += 1
                            
                            if quartile == (2, 2):
                                for i in range(6, 9):
                                    for j in range(6, 9):
                                        for k in self.potential_numbers[i][j]:
                                            if k == num:
                                                num_count += 1
                            
                            if num_count == 1:
                                self.potential_numbers[row][column].clear()
                                self.potential_numbers[row][column].append(num)
                            
                            num_count = 0

                            for i in range(9):
                                for j in self.potential_numbers[i][column]:
                                    if j == num:
                                        num_count += 1

                                for j in self.potential_numbers[row][i]:
                                    if j == num:
                                        num_count += 1

                            if num_count == 1:
                                self.potential_numbers[row][column].clear()
                                self.potential_numbers[row][column].append(num)
                        
    def flush(self):
        for row in range(9):
            for column in range(9):
                self.potential_numbers[row][column].clear()

    def confirm_valid(self):
        for row in range(9):
            for column in range(9):
                if self.grid[row][column] == 0:
                    return False
                else:
                    return True
=======
    def flush(self):
        for row in range(9):
            for column in range(9):
                self.potential_numbers[row][column].clear()
>>>>>>> 30ae5fbbef4f84be40308d7ebfb3bd57a6fc8ecd
