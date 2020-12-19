"""
Write a function that takes in the head of a Singly
Linked List and an integer 'k', shifts the list in
place (ie doesnt create a brand new list) by 'k' 
positions, and returns its new head.

Shifting a Linked List means moving its nodes forward 
or backward and wraping them around the list where 
appropriate. For example, shifting a Linked List forward
by one position would make its tail become the head of 
the new linked list.

Whether nodes are moved forward or backward is determined
by whether 'k' is positive or negative.

Each Linked List has an integer 'value' as well as a 'next'
node pointing to the next node in the list or to None/null
if its the tail of the list.

Assume that the input Linked List will always have at least
one node; in other words, the head will never be None/null.
"""

class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None


def shift_linked_list(head, k):
  list_len = 1
  list_tail = head
  while list_tail.next is not None:
    list_tail = list_tail.next
    list_len += 1

  offset = abs(k) % list_len
  if offset == 0:
    return head
  
  new_tail_pos = list_len - offset if k > 0 else offset

  for i in range(1, new_tail_pos)
    new_tail = new_tail.next

  new_head = new_tail.next
  new_tail.next = None
  new_head.next = head

  return new_head

