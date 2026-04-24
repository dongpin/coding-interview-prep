from python.basic_algorithm.dc_selection import kthSmallest, median_of_medians, quickSort

arr = [9, 8, 7, 6, 5, 0, 1, 2, 3, 4]


def test_quick_sort():
    assert quickSort(arr) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_kth_smallest():
    assert [kthSmallest(arr, i) for i in range(1, 11)] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_median_of_medians():
    assert [median_of_medians(arr, i) for i in range(10)] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
