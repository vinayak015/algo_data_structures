"""
Binary Search Algo
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    arr = [5, 7, 9, 11, 15, 20]
    key = 15
    print(binary_search(arr, key))