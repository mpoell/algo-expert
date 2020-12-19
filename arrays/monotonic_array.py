"""
Write a funciton that takes in an array of integers
and returns a boolean representing whether the array is
monotonic.

An array is said to be monotonic if its elements, from
left to right, are entirely non-increasing or 
entirely non-decreasing
"""
#Time: O(n)
#Space: O(1)
def monotonic_array(array):
  if len(array) == 0:
    return True
    
  #Case: First n nums are equal
  ptr = 1
  while ptr < len(array):
    diff = array[ptr] - array[ptr - 1]

    # Increasing
    if diff > 0:
      while ptr < len(array):
        diff = array[ptr] - array[ptr - 1] 
        if diff < 0:
          return False
        ptr += 1
      return True    

    # Decreasing
    elif diff < 0:
      while ptr < len(array):
        diff = array[ptr] - array[ptr - 1]
        if diff > 0:
          return False
        ptr += 1
      return True

    elif diff == 0:
      ptr += 1
  
  return True


def main():
  array = [1,1,1,1,1,1]
  print(monotonic_array(array))

if __name__ == "__main__":
  main()