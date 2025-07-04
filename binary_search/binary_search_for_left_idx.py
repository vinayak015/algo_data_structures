"""
Binary Search Algo to find out left most idx in a repeated arr, if the key is not present then it will return the right most index where the key should be inserted.
"""

def binary_search(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if target <= arr[mid]:
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    arr = [5, 7, 9, 11, 15, 20]
    key = 15
    print(binary_search(arr, key))