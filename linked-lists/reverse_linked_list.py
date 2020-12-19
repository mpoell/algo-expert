"""
Write a funciton that takes in a head of a Singly
Linked List, reverses the lsit in place (ie. doesnt
create a brand new list), and returns its new head.

Each LinkedList node has an integer 'value' as well
as a 'next' node pointing to the next node in the 
list or to None if it's the tail of the list.

Assume that the input LinkedList  will always have
at least one node; on other words, the head will
never be None.
"""


def reverse_linked_list(head):
  p1, p2 = None, head
  while p2 is not None:
    p3 = p2.next
    p2.next = p1
    p1 = p2
    p2 = p3