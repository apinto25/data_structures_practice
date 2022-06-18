class ListQueue:
    def __init__(self):
        self.items = []
        self.size = len(self.items)

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size = len(self.items)

    def dequeue(self):
        data = self.items.pop()
        self.size = len(self.items)
        return data

    def traverse(self):
        for item in reversed(self.items):
            print(item)
