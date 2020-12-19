"""
Given an array of distinct positive integers representing
coin demoninations and a single non-negative integer n
representing a target amount of money, write a function that
returns the number of ways to make change for that target
amount using the given coin denominations.

Unlimited amount of coins available at your disposal.
"""

# Time O(nd) | Space O(n)
def min_num_coins(n, denoms):
  numOfCoins = [float('inf') for i in range(n + 1)]
  numOfCoins[0] = 0
  for denom in denoms:
    for amount in range(len(numOfCoins)):
      if denom <= amount:
        numOfCoins[amount] = min(numOfCoins[amount], 1 + numOfCoins[amount - denom])
  return numOfCoins[n] if numOfCoins[n] != float('inf') else -1
  

def main():
  n = 11
  denoms = [1, 5, 10]
  print(f"{num_ways(n, denoms)} Coins")

if __name__ == "__main__":
  main()