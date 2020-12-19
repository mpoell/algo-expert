"""
Write a function that takes in the head of a Singly
Linked List and an integer k, rearranges the list in 
place around nodes with value k, and returns its new
head.

Rearranging a Linked List around nodes with the value
k means moving all nodes with a value smaller than k
before all nodes with value k and moving all nodes with
a value greater than k after all nodes with value k.

All moved nodes should maintain original relative ordering
if possible.

Note that the linked list hsould be rearranged even if it 
doesnt have any nodes with value k.

Each LinkedList node has an integer value as well as a next
node pointing to the next node in the list or to None/null
if its the tail of the list.

Assume the input LinkedList will always have at least one
node, in other words, the head will never be None/null.
"""

def rearrange_linked_list(head, k):
  lesser_head = None
  lesser_tail = None
  equal_head = None
  equal_tail = None
  greater_head = None
  greater_tail = None

  node = head
  while node is not None:
    if node.value < k:
      lesser_head, lesser_tail = grow_linked_list(lesser_head, lesser_tail, node)
    elif node.value == k:
      equal_head, equal_tail = grow_linked_list(equal_head, equal_tail, node)
    else:
      greater_head, greater_tail = grow_linked_list(greater_head, greater_tail, node)

    prev_node = node
    node = node.next
    prev_node.next = None

  first_head, first_tail = connect_linked_lists(lesser_head, lesser_tail, equal_tail, equal_tail)
  final_head, _ = connect_linked_lists(equal_head, equal_tail, greater_head, greater_tail)
  return final_head
  
def grow_linked_list(head, tail, node):
  new_head = node if head is none else head
  new_tail = node 

  if tail is not None:
    tail.next = new_tail

  return (new_head, new_tail)


def connect_linked_lists(head_one, tail_one, head_two, tail_two):
  new_head = head_two if head_one is None else head_one
  new_tail = tail_one if tail_two is None else tail_two

  if tail_one is not None:
    tail_one.next = head_two
  
  return(new_head, new_tail)


class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None