from doubly_linked_list import DoublyLinkedList


class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = None
    self.storage = DoublyLinkedList()
    self.index = self.capacity-1

  # def __len__(self):
  #   return self.size

  def getNth(self, tail_node, index): 
    current = tail_node # Initialise temp 
    count = self.capacity-1 # Index of current node 
    print('index in getNth')
    print(index)
    print(count)
    # Loop while end of linked list is not reached 
    while (current): 
        if (count == index): 
            return current 
        count -= 1
        current = current.prev

    ## start with e, d, c, b, a
    ## index [last] is capacity - 1 (a) (tail node)
    ## e, d, c, b, f
    ## capacity [-2] is second oldest element, b

    # if we get to this line, the caller was asking 
    # for a non-existent element so we assert fail 


  def append(self, item):
    # Need to maintain a DLL of the length of the capacity
    # Continue adding to DLL until it matches capacity.
    # print('in append')
    # print('item')
    # print(item)
    # print(self.capacity)
    if self.storage.length < self.capacity:
      self.storage.add_to_head(item)
      print(self.storage.length)
      # first pass a
      # second pass a, b
      # 3rd a, b, c
      # etc, etc. Adding nodes to end end of list ensures order is kept.
    # Once limit is reached. the oldest node (the head), must be removed, and another added to the tail
      # self.storage.remove_from_tail()
      # self.storage.add_to_head(item)
    else:
      if self.index > 0:
        node_placement = self.getNth(self.storage.tail, self.index)
        # print('node value')
        # print(node_placement.value)
        node_placement.value = item
        self.index = self.index-1
        # print('else')
        # print(self.index)
      else: 
        # print('resetting index')
        self.index = self.capacity-1
        self.storage.remove_from_head()
        self.storage.add_to_head(item)


    

  def get(self):
    # Note:  This is the only [] allowed
    list_buffer_contents = []

    # Start at tail, and grab the last elements based upon storage
    count = 0
    current = self.storage.tail
    while count < self.capacity and current is not None:
      list_buffer_contents.append(current.value)
      current = current.prev
      count +=1
    return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity-1
    self.storage = []
    self.index = 0

  def append(self, item):
    if len(self.storage) <= self.capacity+1:
      #Building out initial array to capacity
      self.storage.append(item)
      self.index = self.index+1
    elif self.index <= self.capacity:
      # Moving down through the array once it's filled
      self.storage[self.index] = item
      self.index = self.index+1
    else:
      ## Resetting index to beginning
      self.index = 0
      self.storage[self.index] = item

      ### a, b, c, d, e
      ### 0, 1, 2, 3, 4

  def get(self):
    pass
