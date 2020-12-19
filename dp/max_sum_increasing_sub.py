"""
Write a function that takes in a non-empty array
of integers and returns the greatest sum that can
be generated form a strictly-increasing subsequence
in the array as well as an array of the numbers in
that subsequence.

A subsequence of an array is a set of numbers that 
arent necessarily adjacent in the array but that are
in the same order as they appear in the array. For 
instance, the numbers [1, 3, 4] form a subsequence
of the array [1, 2, 3, 4], and so do the numbers
[2, 4]. Note that a single number in an array and 
the array itself are both valid subsequences of the
array.

Assume that there will only be one increasing 
subsequence with the greatest sum.
"""

# Time O(n^2) | Space O(n)
def max_sum_increasing_subsequence(array):
  sequences = [None for x in array]
  sums = [num for num in array]
  max_sum_idx = 0
  for i in range(len(array)):
    current_num = array[i]
    for j in range(0, i):
      other_num = array[j]
      if other_num < current_num and sums[j] + current_num >= sums[i]:
        sums[i] = sums[j] + current_num
        sequences[i] = j
      if sums[i] >= sums[max_sum_idx]:
        max_sum_idx = i
  return[sums[max_sum_idx], build_sequence(array, sequences, max_sum_idx)]


def build_sequence(array, sequences, current_idx):
  sequence = []
  while current_idx is not None:
    sequence.append(array[current_idx])
    current_idx = sequences[current_idx]
  return(list(reversed(sequence)))


def main():
  array = [10, 70, 20, 30, 50, 11, 30]
  print(max_sum_increasing_subsequence(array))

if __name__ == "__main__":
  main()