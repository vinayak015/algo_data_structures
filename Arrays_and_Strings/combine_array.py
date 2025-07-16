"""
Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.
"""

def combine_arr(arr1, arr2):
    i = 0
    j = 0
    ans = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
    return ans

print(combine_arr([1, 4, 7, 20], [3, 5, 6]))