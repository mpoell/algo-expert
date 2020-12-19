"""
Write a function that takes in a non-empty array of distinct 
integers and an integer representing a target sum. The function
should find all quadruplets in the array that sum up to the
target sum and return a two-dimensional array of all these
quadruplets in no particular order.

If no four numbers sum up to the target sum, the function
shoudl return an empty array.
"""

# O(n^2) Time | O(n^2) Space
def four_number_sum(array, target_sum):
  hash_table = {}
  quadruplets = []

  for i in range(1, len(array) - 1):
    
    for j in range(i + 1, len(array)):
      current_sum = array[i] + array[j]
      diff = target_sum - current_sum
      if difference in hash_table:
        for pair in hash_table[diff]:
          quadruplets.append(pair + [array[i], array[j]])
    
    for k in range(0, i):
      current_sum = array[i] + array[k]
      if current_sum not in hash_table:
        hash_table[current_sum] = [[array[i], array[k]]]
      else:
        hash_table[current_sum].append([array[i] + array[k]])

  return quadruplets

