"""
Takes a non-empty array of distinct integers and an 
integer representing a target stum. If any two numbers 
in the input array sum up to the target sum, the function
should return them in an array, in any order. if no two numbers
sum up to the target sum, the function should return an 
empty array.
"""


# Time: O(n^2)
# Space: O(1)
def two_number_sum_1(array, targetSum):
    for i, num1 in enumerate(array):
        for j, num2 in enumerate(array):
            if i == j:
                continue
            elif num1 + num2 == targetSum:
                return [num1, num2]
    return []


# Time: O(N)
# Space: O(N)
def two_number_sum_2(array, target_sum):
    nums = {}
    for X in array:
        match = target_sum - X
        if match in nums:
            return [X, match]
        else:
            nums[X] = True


# Time: O(nlogn)
# Space: O(1)
def two_number_sum_3(array, target_sum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        result = array[left] + array[right]
        if result == target_sum:
            return [array[left], array[right]]
        elif result > target_sum:
            right -= 1
        else:
            left += 1

    return []



def main():
    arr = [1,2,3,4,5,6]
    target = 3

    print(two_number_sum_1(arr, target))
    print(two_number_sum_2(arr, target))
    print(two_number_sum_3(arr, target))


if __name__ == "__main__":
    main()