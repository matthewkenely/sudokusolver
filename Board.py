from random import randint
from math import ceil

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
    
    def scrape_potential_numbers(self):
        appended = False

        for row in range(9):
            for column in range(9):
                quartile = (row // 3, column // 3)

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

        for row in range(9):
            for column in range(9):
                if len(self.potential_numbers[row][column]) == 1:
                    self.grid[row][column] = self.potential_numbers[row][column][0]

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