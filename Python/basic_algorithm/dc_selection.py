"""
    Quick sort, randomization selection, deterministric selection (median of medians)
"""

import random

# Quick Sort


def quickSort(arr):
    return qSort(arr, 0, len(arr) - 1)


def qSort(arr, left, right):
    if left < right:
        p = random.randint(left, right)
        newIndex = partition(arr, left, right, p)
        qSort(arr, left, newIndex - 1)
        qSort(arr, newIndex + 1, right)
    return arr

# Quick selection: Find kth smallest element in unsorted array


def kthSmallest(arr, k):
    return quickSelect(arr, 0, len(arr) - 1, k - 1)


def partition(arr, left, right, p):
    pValue = arr[p]
    arr[p], arr[right] = arr[right], arr[p]
    j = left
    for i in range(left, right):
        if arr[i] < pValue:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[right], arr[j] = arr[j], arr[right]
    return j


def quickSelect(arr, left, right, k):
    if left == right:
        return arr[left]

    p = random_pivot(left, right)
    newIndex = partition(arr, left, right, p)
    if newIndex == k:
        return arr[newIndex]
    if k < newIndex:
        right = newIndex - 1
    else:
        left = newIndex + 1
    return quickSelect(arr, left, right, k)


def random_pivot(lo, hi):
    return random.randint(lo, hi)

# deterministic selection: median of medians


def median_of_medians(arr, k):

    if len(arr) == 0:
        return
    # divide list into sublists of length 5
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    # sort each sublist and pick up the medians
    medians = [sorted(s)[len(s) // 2] for s in sublists]
    #
    if len(medians) <= 5:
        # nlogn median
        pivot = sorted(medians)[len(medians) // 2]
    else:
        # recursively call to find median
        pivot = median_of_medians(medians, len(medians) // 2)

    # partitioning
    lows = [i for i in arr if i < pivot]
    highs = [i for i in arr if i > pivot]
    # if all element are distinct
    # pivots = [i for i in arr if i == pivot]

    # index of pivot
    p = len(lows)
    if k < p:
        return median_of_medians(lows, k)
    elif k > p:
        return median_of_medians(highs, k - p - 1)
    else:
        # pivot = k
        return pivot


if __name__ == '__main__':
    arr = [9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
    print(quickSort(arr))
    print([kthSmallest(arr, i) for i in range(1, 11)])
    print([median_of_medians(arr, i) for i in range(10)])
