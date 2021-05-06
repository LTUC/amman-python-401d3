# Define Node
class Node():
  def __init__(self, data=None):
      self.data = data
      self.next = None
  # use a magic method so when you print node you see it's value
  def __str__(self):
    return self.data

# Define linked list
class Linked_list():
  # Constructor
  def __init__(self):
    """ """
    self.head = None
  # define your append method
  def append (self, data):
    new_node = Node(data)
    # Once we have a head 
    if self.head :
      current = self.head # set our current pointer to the head
      # while there is a following node that's not None
      while (current.next):
        # move to the next node
        current = current.next
      
      # Assign new_node to current.next
      current.next = new_node
    else:
      #Assign new_node to self.head 
      self.head = new_node
  # __str__ , __repr__
  def __str__(self):
    """ Returns a string representaiton of the linked list
        1 -> 3 -> 4
    """
    # step 0 - create a new empty string
    output = ""

    # step 1 iterate over each node
    current = self.head
    while current:
      # step 2 - append each data to the string
      output += f" {current.data} ->"
      # step 2b:  move to the next item
      current = current.next
    output += " None"

    # step 3 - return the final string
    return output


# Write program here
if __name__ == "__main__":
  item = Node('Manar')
  linked = Linked_list()
  linked.head = item
  # item.data = 'Manar'
  print(item.data)
  print(linked.head)
  linked.append("Muhannad")
  linked.append("Hisham")
  print(linked.__str__())

# I am finally here
