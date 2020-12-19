"""
Bubble Sort Implementation
"""

# Time: O(n) | Space O(1)


def bubbleSort(array):
    while True:
        for i in range(1, len(array)):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
        if isSorted(array):
            return array


def isSorted(array):
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            return False
    return True


array = [8, 5, 2, 9, 5, 6, 3]

print(bubbleSort(array))
