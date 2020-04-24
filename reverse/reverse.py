class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next


class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)

    self.head = node

  def contains(self, value):
    # if not self.head:
    #   return False
    # get a reference to the node we're currently at; update this as we
    # traverse the list
    current = self.head
    # check to see if we're at a valid node
    while current:
      # return True if the current value we're looking at matches our
      # target value
      print(current)
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self, node, prev):
    # exit case when list has no elements
    if node == None: 
      return node 
    # exit case when list has 1 element, already sorted
    if node.next_node == None:
      self.head = node
      return node
    print('first pass')
    print(node, node.next_node, node.next_node.next_node)
    # grabbing next node to pass before it gets changed
    temp = node.next_node
    # setting current node to point backwards
    node.set_next(prev)
    # setting future previous node, to be the next node off of temp
    prev = temp
    self.reverse_list(node, prev)

# None -> 1 -> 2 -> 3 -> 4 -> 5
    # 1, None
    # None < - 1 -> 2 -> 3 -> 4 -> 5
# 