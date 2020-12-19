"""
Write a function that takes in the heads of the two 
Singly Linked Lists that are in sorted order, 
respectively. The function should merge the lists 
in place (ie it shouldnt create a brand new list)
and return the head of the merged list; the merged
list should be in sorted order.

Each LinkedList node has an integer 'value' as well
as a 'next' node pointing to the next node in the 
list or to None if it's the tail of the list.

Assume that the input LinkedLists will always have
at least one node; on other words, the heads will
never be None.
"""

def merge_linked_lists(head_one, head_two):
  