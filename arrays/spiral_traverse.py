"""
Write a function that takes in an NxM 
two-dimensional array (can be square
shaped when n==m) and returns a one-dimensional
arrayof all the array's elements in spiral order.

Spirat order starts at the top left corner of the
two-dimensional array, goes to the right, and proceeds
in a spiral pattern all the way until every elment
has been visited
"""

  
# O(n) time | O(n) space
def spiral_traverse(array):
  result = []
  spiral_fill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
  return result

def spiral_fill(array, start_row, end_row, start_col, end_col, result):
  if start_row > end_row or start_col > end_col:
    return
  
  for col in range(start_col, end_col + 1):
    result.append(array[start_row][col])

  for row in range(start_row + 1, end_row + 1):
    result.append(array[row][end_col])

  for col in reversed(range(start_col, end_col)):
    result.append(array[end_row][col])
  
  for row in reversed(range(start_row + 1, end_row)):
    result.append(array[row][start_col])

  spiral_fill(array, start_row + 1, end_row - 1, start_col + 1, end_col - 1, result)

  









def main():
  array=[
    [27, 12, 35, 26],
    [25, 21, 94, 11],
    [19, 96, 43, 56],
    [55, 36, 10, 18],
    [96, 83, 31, 94],
    [93, 11, 90, 16] ]
  
  print(spiral_traverse(array))

if __name__ == "__main__":
  main()
