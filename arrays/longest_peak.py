"""
Write a function that takes in an array of integers
and returns the length of the longest peak in the array.

A peak is defined as adjacent integers in the array that 
are strictly increasing until they reach a tip (highest value
in the peak), at which point they become stricly decreasing. At
lease three integers are required to form a peak.

For example, the integers [1, 4, 10, 2] form a peak, but the 
integers [4, 0, 10] don't and neither do the integers [1, 2, 2, 0].
Similarly, the integers [1, 2, 3] dont form a peak because there 
arent any strictly decreasing integers after the 3.
"""

# O(n) time | O(n) space
def longest_peak(array):
  longest = []

  p1, p2 = 0, 1
  result = [array[p1]]

  while p2 < len(array):
    if array[p2] > array[p1]:
      result.append(array[p2])
      p2 += 1
      p1 += 1
      while array[p2] > array[p1]:
        result.append(array[p2])
        p2 += 1
        p1 += 1

      if array[p2] == array[p1]:
        p2 += 1
        p1 += 1
        result = [array[p1]]

      elif array[p2] < array[p1]:
        result.append(array[p2])
        p2 += 1
        p1 += 1
        while array[p2] < array[p1]:
          result.append(array[p2])
          p2 += 1
          p1 += 1
    
      if result[0] < max(result) and result[-1]:
        if len(result) > len(longest):
          longest = result
      
      result = []
      p2 += 1
      p1 += 1


    else:
      p2 += 1
      p1 += 1

  return longest



def main():
  array = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
  print(longest_peak(array))

if __name__ == "__main__":
  main()