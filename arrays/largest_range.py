"""
Write a function that takes in an array
of integers and returns an array of length 2
representing the largest range of integers
contained in that array.

The first number in the output array should be
the first number in the range, while the second number
should be the last number in the range.

A range of nujmbers i s defined as a set of nujmbers
that come right after each other in the set of real 
integers. FOr instance, the output array [2, 6] 
represents the range {2, 3, 4, 5, 6}, which is a range
of length 5. Note that numbers dont need to be sorted
or adjacent in the input array in order to form a range.

Assume that there will only be one largest range.
"""


# Time O(n) | Space O(n)
def largest_range(array):
  best_range = []
  longest_len = 0
  nums = {}

  for num in array:
    nums[num] = True

  for num in array:
    if not nums[num]:
      continue
    nums[num] = False
    tmp_len = 1
    left = num - 1
    right = num + 1
    while left in nums:
      nums[left] = False
      tmp_len += 1
      left -= 1
    while right in nums:
      nums[right] = False
      tmp_len += 1
      right += 1
    if tmp_len > longest_len:
      longest_len = tmp_len
      result = [left + 1, right - 1]

  return result



def main():
  array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6] # => [0,7]
  print(largest_range(array))

if __name__ == "__main__":
  main()

