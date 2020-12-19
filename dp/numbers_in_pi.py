"""
Given a string representation of the first n
digits of Pi and a list of positive integers
(string format), write a function that returns
the smallest number of spaces that can be added
to the n digits of Pi such that all resulting 
numbers are found in the lsit of integers.

Note that a single number can appear multiple 
times in the resulting numbers. For example, if
Pi is "3141" and the numbers are ["1", "3", "4"],
the number "1" is allowed to appear twice in the
list of resulting numbers after three spaces are
added: "3 | 1 | 4 | 1".

If no number of spaces to be added exists such that
all resulting numbers are found in the list of 
integers, the function should return -1
"""


def numbersInPi(pi, numbers):
    numbersTable = {number: True for number in numbers}
    minSpaces = getMinSpaces(pi, numbersTable, {}, 0)
    return -1 if minSpaces == float("inf") else minSpaces


def getMinSpaces(pi, numbersTable, cache, idx):
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces = float("inf")
    for i in range(idx, len(pi)):
        prefix = pi[idx: i + 1]
        if prefix in numbersTable:
            minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)
    cache[idx] = minSpaces
    return cache[idx]


testCase = {
  "pi": "3141592653589793238462643383279",
  "numbers": [
    "314159265358979323846",
    "26433",
    "8",
    "3279",
    "314159265",
    "35897932384626433832",
    "79"
  ]
}