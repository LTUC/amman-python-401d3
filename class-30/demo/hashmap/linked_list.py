class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    
    def display(self):
        output = []
        # traverse linked list and add to output
        current = self.head
        while current:
            output.append(current.value)
            current = current.next
        return output
    