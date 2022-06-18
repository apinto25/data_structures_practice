import random
from custom_array import Array


class Cube:

    def __init__(self, rows, columns, depth, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns)
            for column in range(columns):
                self.data[row][column] = Array(depth, fill_value)

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def get_depth(self):
        return len(self.data[0][0])

    def __getitem__(self, row, column, depth):
        return self.data[row][column][depth]

    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                for depth in range(self.get_depth()):
                    result += str(self.data[row][column][depth]) + " "
                
                result += "\n"
            result += "\n"
        return result.strip()

    def random_fill(self, min=0, max=10):
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                for depth in range(self.get_depth()):
                    self.data[row][column][depth] = random.randint(min, max)
