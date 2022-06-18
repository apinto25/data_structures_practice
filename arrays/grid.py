import random

from custom_array import Array


class Grid:

    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                result += f"{str(self.data[row][column])} "

            result += "\n"
        return result.strip()

    def random_fill(self, min=0, max=10):
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                self.data[row][column] = random.randint(min, max)
            