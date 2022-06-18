import random


class Array:

    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for _ in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def random_fill(self, min=0, max=10):
        for index in range(len(self.items)):
            self.__setitem__(index, random.randint(min, max))

    def sum_items(self):
        return sum(self.items)
