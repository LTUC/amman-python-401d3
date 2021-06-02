###########################
# [Optional] explain what range is doing under the hood
###########################

# range_gen = range(100)

# print(type(range_gen))

# iterator = iter(range_gen)

# print(type(iterator))

# while True:

#     try:
#         i = next(iterator)
#     except StopIteration:
#         break

###########################

# generator a function that knows how to return the next value of a sequence
# it give us only one value at a time
# generators are iterables because we can call next() to get the next value in the sequence

range_gen = range(3)
iterator = iter(range_gen)

print(next(iterator)) # 0
print(next(iterator)) # 1
print(next(iterator)) # 2
# print(next(iterator)) # no more values

# it's lazy so it will only do the work when the value is needed and not before

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):  # Big O(1)
        node = Node(value)

        if self.head:
            node.next = self.head

        self.head = node
    
    def __str__(self):
        string = ""
        current = self.head
        while current:
            string += f"[{current.value}] -> "
            current = current.next
        string += "None"
        return string

    def __iter__(self):
        current = self.head
        while current:
            yield current.value # yield will pause the function and return the value on RHS of yield
            current = current.next # will resume here when next() is called

new_list = LinkedList()
print(new_list)
new_list.insert(5)
print(new_list)
new_list.insert(4)
print(new_list)
# HEAD = [1] -> [2] -> [3]

# [0]->[1] -> [2] -> [3]

# HEAD = [0]->[1] -> [2] -> [3]

list_iter = iter(new_list)
print(next(list_iter))
print(next(list_iter))

# for item in new_list:
#     print(item)