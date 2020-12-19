"""
You're given an array of integers and an integer.
Write a funciton that moves all instances of that
integer in the array to the end of the array
and returns the array

This function shoudl perform this in place, and
doesn't need to maintain the order of the other
integers.
"""

#Time: O(nlogn)
#Space: O(1)
def move_element_to_end(array, tgt_num):
  
  array.sort()

  for i, num in enumerate(array):
    if num != tgt_num:
      array.append(array.pop(i))
    else:
      array.reverse()
      return array  


#Time: O(n)
#Space: O(1)
def move_element_to_end2(array, tgt_num):
  L = 0
  R = len(array) - 1

  while L != R:
    if array[L] == tgt_num:
      array[L], array[R] = array[R], array[L]
      R -= 1
    else: 
      L += 1
    
  return array


def main():
  array = [12,1,2,2,2,3,4,2]
  tgt_num = 2

  print(move_element_to_end2(array, tgt_num))

if __name__ == "__main__":
  main()