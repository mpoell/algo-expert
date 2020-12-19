"""
Write a function that takes in the head of a Singly
Linked List that contains a loop (in other words, the
lists tail node points to some node in the list instead
of None). The function should return the node (the actual
node, not just its value) from which the loop originates
in constant space.

Each LinkedList node has an integer 'value' as well as 
a 'next' node pointing to the next node in the list.
"""


class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None


# Time O(N) | Space O(1)
def find_loop(head):
  first = head.next
  second = head.next.next
  while first != second:
    first = first.next
    second = second.next.next
  first = head
  while first != second:
    first = first.next
    second = second.next
  return first

