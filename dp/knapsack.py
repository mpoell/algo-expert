"""
You're given an array of arrays where each subarray
holds two integer values and represents an item; 
the first integer is the item's value, and the second
is the item's weight. You're also given an integer 
representing the maximum capactiy of a knapsack that 
you have.

Your goal is to fit items in your knapsack without
having the sum of their weights exceed the knapsack's 
weight capacity, all while maximizing their combined 
value. Note that you only have one of each item at
your disposal.

Write a function that returns the maximized combined
value of the items that you should pick as well as an 
array of the indices of each item picked.

If there are multiple combinations of items that 
maximize the total value in the knapsack, your function
can return any of them.
"""

# Time O(nc) | Space O(nc)
def knapsack_problem(items, capacity):
  knapsack_values = [[0 for x in range(capacity + 1)] for y in range(len(items) + 1)]
  for i in range(1, len(items) + 1):
    weight = items[i - 1][1]
    value = items[i - 1][0]
    for j in range(capacity + 1):
      if weight > j:
        knapsack_values[i][j] = knapsack_values[i - 1][j]
      else:
        knapsack_values[i][j] = max(knapsack_values[i - 1][j], knapsack_values[i - 1][j - weight] + value)
  return [knapsack_values[-1][-1], get_indicies(knapsack_values, items)]


def get_indicies(knapsack_values, items):
  sequence = list()
  i = len(knapsack_values) - 1
  j = len(knapsack_values[0]) - 1
  while i > 0:
    if knapsack_values[i][j] == knapsack_values[i - 1][j]:
      i -= 1
    else:
      sequence.append(i - 1)
      j -= items[i - 1][1]
      i -= 1
    if j == 0:
      break
  return list(reversed(sequence))


def main():
  items = [
    [465, 100],
    [400, 85],
    [255, 55],
    [350, 45],
    [650, 130],
    [1000, 190],
    [455, 100],
    [100, 25],
    [1200, 190],
    [320, 65],
    [750, 100],
    [50, 45],
    [550, 65],
    [100, 50],
    [600, 70],
    [255, 40]
  ]
  capacity = 200
  
  print(knapsack_problem(items, capacity))

if __name__ == "__main__":
  main()
