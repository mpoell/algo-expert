"""
Takes a non-empty array of distinct integers and an 
integer representing a target stum. If any three numbers 
in the input array sum up to the target sum, the function
should return them in an array, in any order. The function should
return all possible triplets. If no three numbers
sum up to the target sum, the function should return an 
empty array.
"""


# Only finds one triplet
def three_number_sum(array, target_sum):
    left = 0
    mid = len(array) // 2
    right = len(array) - 1
    flip1 = True
    flip2 = True

    array.sort()

    while mid != right and mid != left:

        total = array[left] + array[mid] + array[right]
        if total == target_sum:
            return[array[left], array[mid], array[right]]
        elif total > target_sum:
            if flip1:
                mid -= 1
                flip1 = False
            else:
                right -= 1
                flip1 = True
        else:
            if flip2:
                mid += 1
                flip2 = False
            else:
                left =+ 1
                flip2 = True

    return []

# Time: O(n^2)
# Space: O(n)
def three_number_sum_1(array, target_sum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == target_sum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            elif current_sum > target_sum:
                right -= 1
                
    return triplets

    




def main():
    #Ans=[-8, 2, 6], [-8, 3, 5], or [-6, 1, 5]
    arr = [-8, -6, 1, 2, 3, 5, 6, 12]
    target = 0

    print(three_number_sum(arr, target))


if __name__ == "__main__":
    main()

