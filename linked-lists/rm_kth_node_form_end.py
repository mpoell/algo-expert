"""
Write a funciton that takes in a head of a Singly Linked List
and an iteger k and removes the kth node from the end of the list.

The removal shoudl be done in place, meaning that the original data
structure should be mutated (no new structure should be created).

Furthermore, the input head of the linked list should remain the 
head of the linked list after the removal is done, even if the head
is the node thats supposed to be removed, your funciton should simply
mutate its 'value' and 'next' pointer. 

Note that your funciton doesnt have to return anything.

You can assume that the input linked list will always have at least
two nodes and, more specifically, at least k nodes.

Each LinkedList will always have at least two node and, more specifically,
at least k nodes.

Each LinkedList node has an integer 'value' as well as a 'next' node 
pointing to the next node in the lsit or to None if it's the tail of
the list.
"""


class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None

# O(N) Time | O(1) space
def remove_kth_node_from_end(head, k):
  counter = 1
  first = head
  second = head

  while counter <= k:
    second = second.next
    counter += 1

  # Case: node to remove is head
  if second is None:
    head.value = head.next.value
    head.next = head.next.next
    return
  
  while second.next is not None:
    second = second.next
    first = first.next
  # first is pointing to the node right before the node we want to remove
  first.next = first.next.next






def main():
  head = 0 # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
  k = 4 # Node '6'