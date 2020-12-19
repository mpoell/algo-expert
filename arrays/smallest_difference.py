"""
Write a function that takes in two non-empty arrays of integers,
finds the pair of numbers (one from each array) whose absolute difference
is closest to zero, and returns an array containing these two numbers,
with the number from the first array in the first poition.

Assume there will only be one pair of numbers with the smallest difference.
"""

#Time: O(n^2)
#Space: (1)
def smallest_difference1(array1, array2):
  smallest_pair = []
  smallest_diff = 999999
  
  for num1 in array1:
    for num2 in array2:
      if abs(num1 - num2) < smallest_diff:
        smallest_pair = [num1, num2]
        smallest_diff = abs(num1 - num2)

  return smallest_pair, smallest_diff


#Time: O(nlogn)
#Space: O(1)
def smallest_difference2(array1, array2):
  array1.sort()
  array2.sort()
  ptr1 = 0
  ptr2 = 0
  smallest_diff = 999999
  current = 999999
  

  while ptr1 < len(array1) and ptr2 < len(array2):
    num1 = array1[ptr1] 
    num2 = array2[ptr2]
    
    if num1 < num2:
      current = num2 - num1
      ptr1 += 1
    elif num2 < num1:
      current = num1 - num2
      ptr2 += 1
    else:
      return [num1, num2]
    
    if current < smallest_diff:
      smallest_diff = current
      smallest_pair = [num1, num2]
    
  return smallest_pair, smallest_diff



  
def main():
  array1 = [-1, 5, 10, 20, 28, 3] 
  array2 = [26, 134, 135, 15, 17]

  print(smallest_difference1(array1, array2))
  print(smallest_difference2(array1, array2))

if __name__ == "__main__":
  main()