"""
Write a function that takes in an array of positive
integers and returns the maximum sum of non-adjacent
elements in the array.

If a sum can't be generated, the function should 
return 0
"""

# Time O(n) | Space O(n)
def max_subset_sum_1(array):
  if not len(array):
    return
  if len(array) == 1:
    return array[0]
  max_sums = array[:]
  max_sums[1] = max(array[0], array[1])
  for i in range(2, len(array)):
    max_sums[i] = max(max_sums[i - 1], max_sums[i - 2] + array[i])
  return maxSums[-1]


# Time O(n) | Space O(1)
def max_subset_sum_2(array):
  if not len(array):
    return
  if len(array) == 1:
    return array[0]
  second = array[0]
  first = max(array[0], array[1])
  for i in range (2, len(array)):
    current = max(first, second + array[i])
    second = first
    first = current
  return first

  

def main():
  array = [75, 105, 120, 75, 90, 135]
  print(max_subset_sum_2(array))

if __name__ == "__main__":
  main()   