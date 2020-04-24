from doubly_linked_list import DoublyLinkedList


class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = None
    self.storage = DoublyLinkedList()
    self.size = 0

  def __len__(self):
    return self.size

  def append(self, item):
    # Need to maintain a DLL of the length of the capacity
    # Continue adding to DLL until it matches capacity.
    if self.storage.length < self.capacity:
      self.storage.add_to_head(item)
      # first pass a
      # second pass a, b
      # 3rd a, b, c
      # etc, etc. Adding nodes to end end of list ensures order is kept.
    # Once limit is reached. the oldest node (the head), must be removed, and another added to the tail
    else:
      self.storage.remove_from_tail()
      self.storage.add_to_head(item)

    

  def get(self):
    # Note:  This is the only [] allowed
    list_buffer_contents = []

    # Start at tail, and grab the last elements based upon storage
    count = 1
    current = self.storage.tail
    while count < self.capacity:
      list_buffer_contents.append(current.value)
      current = current.prev
      count +=1
    return list_buffer_contents

# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#   def __init__(self, capacity):
#     pass

#   def append(self, item):
#     pass

#   def get(self):
#     pass
