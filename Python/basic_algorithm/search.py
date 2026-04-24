# Linear Search

def linear_search(arr, key):
    for i, v in enumerate(arr):
        if v == key:
            return i
    return -1


# Binary Search

def binary_search(arr, key):
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        median = lo + (hi - lo) // 2
        if arr[median] < key:
            lo = median + 1
        elif arr[median] == key:
            return median
        else:
            hi = median - 1
    return -1


# Ternary Search

def _ternary(arr, key, lo, hi):
    if lo <= hi:
        mid1 = lo + (hi - lo) // 3
        mid2 = hi - (hi - lo) // 3
        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2
        if key < arr[mid1]:
            return _ternary(arr, key, lo, mid1 - 1)
        elif key > arr[mid2]:
            return _ternary(arr, key, mid2 + 1, hi)
        else:
            return _ternary(arr, key, mid1 + 1, mid2 - 1)
    return -1


def ternary_search(arr, key):
    return _ternary(arr, key, 0, len(arr) - 1)
