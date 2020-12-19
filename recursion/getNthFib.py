"""
The Fibonacci sequence is defined as follows: the first 
number of the sequence is 0, the second number is 1, and
the nth number is the sum of the (n-1)th and (n-2)th 
numbers.

Write a function that takes in an integer n and returns
the nth Fibonacci number.
"""

# Naive Recursive
# Time: O(2^n) | Space O(n)


def getNthFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)


# Memoized Recursive
# Time: O(n) | Space O(n)
def getNthFib(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
    return memoize[n]


# Iterative Solution
# Time: O(n) | Space O(1)
def getNthFib(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]
