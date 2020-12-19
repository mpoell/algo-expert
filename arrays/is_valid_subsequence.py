"""
Given two non-empty arrays of integers, write
a funciton that determines whethere the second
array is a subsequence of the first one.
"""


# Time: O(n)
# Space: O(1)
def is_valid_subsequence(array, sequence):
    arr_ptr = 0
    seq_ptr = 0

    while arr_ptr < len(array) and seq_ptr < len(sequence):
        if array[arr_ptr] == sequence[seq_ptr]:
            seq_ptr += 1
        arr_ptr += 1
                    

    return seq_ptr == len(sequence)


def main():
    arr = [5, 1, 22, 25, 6, -1, 8, 10]
    seq = [1, 6, -1, 10]

    print(is_valid_subsequence(arr, seq))

if __name__ == "__main__":
    main()