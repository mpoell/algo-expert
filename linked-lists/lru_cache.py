"""
Implement an LRUCache class for a Least Recently Used (LRU) cache.
The class should support:
  - Inserting key-value pairs with the 'insert_key_value_pair' method.
  - Retrieving a key's value with the get_value_from_key method.
  - Retrieving the most recently used(the most recently inserted or
      retrieved) key with the get_most_recent_key method

Each of these methods should run in constant time. 

Additionally, the LRUCache class should store a max_size property to set
the size of the cache, which is passed in an an argument during
instantiation. This size represents the maximum number of key-value pairs
that the cache can store at once. If a key-value pair is inserted in the 
cache when it has reached maxmum capacity, the least recently used key-value
pair should be evicted from the cache and no longer retrievable; the newly 
added key-value pair should effectively replace it.

Note that inserting a key-value pair with an already existing key should
simply replace the key's value in the cache with the new value and shouldn't
evict a key-value pair if the cache is full. Lastly, attempting to retrieve a 
value from a key that isnt in the cache should return None/null. 
"""


class LRUCache:
  def __init__(self, max_size):
    self.max_size = max_size or 1
    self.size = 0
    self.cache = DoublyLinkedList()
    self.in_lru = {}

  def insert_key_value_pair(self, key, value):
    new_node = Node(key, value)
    if self.in_lru[key]: # Node already in LRU Cache
      self.cache.remove_node_with_key(key)
      self.cache.insert_at_position(1, new_node)
    else: # Node not in LRU Cache
      self.cache.set_head(node)
      self.in_lru[key] = True
      self.size += 1
      if self.size > self.max_size:
        self.cache.remove(self.cache.tail)
        self.size -= 1
    
  def get_value_from_key(self, key):
    return self.cache.get_value_by_key(key)

  def get_most_recent_key(self):
    return self.cache.head


class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.prev = None
    self.next = None

  def update_value(self, new_value):
    self.value = new_value
    return


class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  # O(1) Time | O(1) Space
  def set_head(self, node):
    if self.head is None:
      self.head = node
      self.tail = node
      return
    self.insert_before(self.head, node)

  def set_tail(self, node):
    if self.tail is None:
      self.head = node
      self.tail = node
      return
    self.insert_after(self.tail, node)

  def insert_before(self, node, node_to_insert):
    if node_to_insert == self.head and node_to_insert == self.tail:
      return
    self.remove(node_to_insert)
    node_to_insert.prev = node.prev
    node_to_insert.next = node
    if node.prev is None:
      self.head = node_to_insert
    else:
      node.prev.next = node_to_insert
    node.prev = node_to_insert

  def insert_after(self, node, node_to_insert):
    if node_to_insert == self.head and node_to_insert == self.tail:
      return
    self.remove(node_to_insert)
    node_to_insert.prev = node
    node_to_insert.next = node.next
    if node.next is None:
      self.tail = node_to_insert
    else:
      node.next.prev = node_to_insert
    node.next = node_to_insert

  def find_position(self, target_node):
    position = 0
    node = self.head
    while node is not None:
      if node.key == target_node.key:
        return position
      node = node.next
      position += 1
    return None

  def insert_at_position(self, position, node_to_insert):
    if position == 1:
      self.set_head(node_to_insert)
      return
    node = self.head
    curr_position = 1
    while node is not None and curr_position != position:
      node = node.next
      curr_position += 1
    if node is not None:
      self.insert_before(node, node_to_insert)
    else:
      self.set_tail(node_to_insert)

  def remove_node_with_key(self, value):
    node = self.head
    while node is not None:
      node_to_remove = node
      node = node.next
      if node_to_remove.key == key:
        self.remove(node_to_remove)

  def get_value_by_key(self, key):
    node = self.head:
    while node is not None:
      if node.key == key:
        return node.value
    return None

  # def update_node_with_key(self, key, new_value):
  #   node = self.head
  #   while node is not None:
  #     node_to_update = node
  #     node = node.next
  #     if node_to_update.key == key:
  #       node_to_update.update_value(new_value)

  def remove(self, node):
    if node == self.head:
      self.head = self.head.next
    if node == self.tail:
      self.tail = self.tail.prev
    self.remove_node_bindings(node)
    
  def contains_node_with_value(self, value):,
    node = self.head
    while node is not None and node.value != value:
      node = node.next
    return node is not None # node == value broke out of while loop
  
  def remove_node_bindings(self, node):
    if node.prev is not None:
      node.prev.next = node.next
    if node.next is not None:
      node.next.prev = node.prev
    node.next = None
    node.prev = None


