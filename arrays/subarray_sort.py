"""
Write a function that takes in an array of at least two
integers and that returns an array of the starting and
ending indices of the smallest subarray in the input
array that needs to be sorted in place in order for the 
entire input array to be sorted (in ascending order).

If the input array is already sorted, the function should
return [-1, 1]
"""

#Wrong Answer
# time O(n^2) | space O(1)
def subarray_sort1(array):
  result = []
  idx = 0

  for i in range(1, len(array) - 1):
    if not(is_ordered(array[i-1], array[i], array[i+1])):
      if array[i] < array[i - 1]:
        idx = i
        while array[idx] < array[idx-1]:
          array[idx], array[idx-1] = array[idx-1], array[idx]
          idx += 1
        result.append(idx)
      elif array[i] > array[i+1]:
        idx = i
        while array[idx] > array[idx+1]:
          array[idx], array[idx+1] = array[idx+1], array[idx]
          idx -= 1
        result.append(idx)
    
  return result
  # return [min(result), max(result)]
def is_ordered1(x, y, z):
  if y >= x and y <= z:
    return True
  return False


# Correct Answer
# Time O(n) | Space O(1)

def subarray_sort(array):
  min_out = float("inf")
  max_out = float("-inf")

  for i in range(len(array)):
    num = array[i]
    if unordered(i, num, array):
      min_out = min(num, min_out)
      max_out = max(num, max_out)

  if min_out == float("inf"):
    return [-1, -1]

  idxL = 0
  idxR = len(array) - 1
  while min_out >= array[idxL]:
    idxL += 1
  while max_out <= array[idxR]:
    idxR -= 1

  return[idxL, idxR]


def unordered(i, num, array):
  if i == 0:
    return num > array[i+1]
  
  if i == len(array) - 1:
    return num < array[i-1]

  return num > array[i + 1] or num < array[i - 1]




def main():
  array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
  print(subarray_sort(array))



if __name__ == "__main__":
  main()