"""
Write a function that takes in an n x m two-dimensional
array and returns a one-dimensional array of all the array's
elements in zigzag order.

Zigzag order starts at the top left forner or the two-dimensional
array, goes down by one element, and proceeds in a zigzag pattern
all the way to the bottom right corner.
"""

def zigzag_traverse(array):
  M = len(array) - 1 
  N = len(array[0]) -1
  m = 1
  n = 0
  result = [array[0][0], array[m][n]]

  down = False
  while [m,n] != [M,N]:
    if down:
      while in_bounds([M, N], diag_down([m, n])):
        m, n = diag_down([m, n])
        result.append(array[m][n])
      down = False
      if m < M:
        m += 1
      elif m == M:
        n += 1
      result.append(array[m][n])
    
    elif not down:
      while in_bounds([M, N], diag_up([m, n])):
        m, n = diag_up([m, n])
        result.append(array[m][n])
      down = True
      if n < N:
        n += 1
      elif n == N:
        m += 1
      result.append(array[m][n])

  return result


def diag_up(coord):
  return [coord[0] - 1, coord[1] + 1]

def diag_down(coord):
  return [coord[0] + 1, coord[1] - 1]

def in_bounds(dimensions, coord):
  if coord[0] >= 0 and coord[0] <= dimensions[0] and coord[1] >= 0 and coord[1] <= dimensions[1]:
    return True
  return False


def main():

  array = [
    [1, 3, 4 ,10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16]
  ]

  # print(diag_up([2, 0]))
  # print(diag_down([0, 2]))
  # print(in_bounds([3, 3], diag_up([2, 0])))

  print(zigzag_traverse(array))

if __name__ == "__main__":
  main()