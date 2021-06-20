from linked_list import LinkedList

class Hashmap:
    """
    This class simulates the functionality of the hashmap.

    Run 'python -m doctest -v hashmap.py' in terminal in action
    Hover over Hashmap class definition to also see doctest in action
    Try breaking expected values and see what happens

    Use doctest WITH unit tests, NOT INSTEAD of unit tests

    Some tests:
    >>> hashmap = Hashmap(1024)
    >>> hashmap.set('ahmad', 30)
    >>> hashmap.set('silent', True)
    >>> hashmap.set('listen', 'to me')
    >>> for item in hashmap._buckets:
    ...     if item:
    ...         item.display()
    [['silent', True], ['listen', 'to me']]
    [['ahmad', 30]]
    """
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size
    

    def _hash(self, key):
        """
        Accepts the key and returns the index where this key should be stored
        """
        sum = 0
        for char in key:
            sum += ord(char)
        h = ( sum * 19) % self.size
        return h
        

    def add(self, key, value):
        index = self._hash(key)

        if not self._buckets[index]:
            self._buckets[index] = LinkedList()

        self._buckets[index].add([key, value])


    def find(self, key):
        """
        Accepts a key and returns the value for the key if it exists in our hashmap
        """
        index = self._hash(key)

        bucket = self._buckets[index]

        # traverse the link list
        current = bucket.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next

        raise KeyError("Key not found", key)

    def delete(self, key):
        """
        Delete the value a the key
        """
        pass

    def contains(self, key):
        """
        Return true if there is a value in the hashmap with that key or false otherwise
        """
        pass
