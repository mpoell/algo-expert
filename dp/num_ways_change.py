# Given an array of distinct positive integers representing 
# coin denominations and a single non-negative integer n
# representing a target amount of money, write a funciton 
# that returns the number of ways to make change for that
# target amount using the given coin denominations.

# Unlimited amount of goins at your disposal

# Time O(nd) | Space O(n)
def num_ways_change (n, denoms):
  ways = [0 for amount in range(n + 1)]
  ways[0] = 1
  for denom in denoms:
    for amount in range(1, n + 1):
      if denom <= amount:
        ways[amount] += ways[amount - denom]
  return ways[n]

def main():
  n = 10
  denoms = [1, 5, 10, 25] 
  print(f"{num_ways_change(n, denoms)} Ways")

if __name__ == "__main__":
  main()