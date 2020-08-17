def linear_search(arr, target):
    for idx, elem in enumerate(arr):
        if elem == target:
            return idx


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    head = 0
    tail = len(arr) - 1

    while head <= tail:
        mid = (head + tail) // 2

        if arr[mid] == target:
            return mid
        else:
            if arr[mid] > target:
                tail = mid -1
            else:
                head = mid + 1

    return -1  # not found
