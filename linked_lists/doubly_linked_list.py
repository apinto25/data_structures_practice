class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def add_front(self, new_data): # Push
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            raise Exception("Previos node must be in the Linked List")

        new_node = Node(new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node

        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def add_end(self, new_data): # Append
        new_node = Node(new_data)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.nead = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
            new_node.prev = current_node
