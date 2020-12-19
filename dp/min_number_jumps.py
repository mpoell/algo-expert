"""
You're given a non-empty array of positive
integers where each integer represents the
maximum number of steps you can take forward
in the array. For example, if the element at
index 1 is 3, you cna go form index 1 to index
2, 3, or 4.

Write a function that returns the minimum number
of jumps needed to reach the final index.

Note that jumping from index i to index i + x
always constitutes one jump, no matter how large
x is.
"""

def min_number_jumps(array):
  jumps = [float("inf") for x in array]
  jumps[0] = 0
  for i in range(1, len(array)):
    for j in range(0, i):
      if array[j] >= i - j:
        jumps[i] = min(jumps[j] + 1, jumps[i])
  return jumps[-1]



def main():
  array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
  print(min_number_jumps(array))

if __name__ == "__main__":
  main()