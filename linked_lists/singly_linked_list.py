class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def add_front(self, new_data): # Push
        """Creates a new Node, add the current head as the next of the new node
        and asign the new head to the LL head."""

        new_head = Node(new_data)
        new_head.next = self.head
        self.head = new_head

    def add_end(self, new_data): # Append
        """Creates a new Node, if the linked list is empty add the node to the
        head, else traverse the linked list until the last node and adds the new
        node as its next node."""

        new_last = Node(new_data)
        if self.head is None:
            self.head = new_last
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_last

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            raise Exception("Previos node must be in the Linked List")

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def remove_first_ocurring_node(self, value):
        """Removes the first occurence of a node which data is the same as the
        given value."""

        current_node = self.head

        if current_node is not None and current_node.data == value:
            self.head = current_node.next
            current_node = None
            return

        while current_node is not None:
            if current_node.data == value:
                break
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None


list1 = SinglyLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list1.head.next = e2
# Link second Node to third node
e2.next = e3

list1.add_front("Sun")
list1.add_end("Thu")

list1.print_list()

list1.remove_first_ocurring_node("Sun") # Removing the head
list1.print_list()

list1.remove_first_ocurring_node("Wed") # Removing node
list1.print_list()

list1.remove_first_ocurring_node("Thu") # Removing last
list1.print_list()
