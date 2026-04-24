
from python.basic_algorithm.sorting import Sorting

test_cases = [([], []), ([1, 2, 3], [1, 2, 3]),
              ([3, 2, 1], [1, 2, 3]),
              ([2, 99, 2, 99, 2], [2, 2, 2, 99, 99]),
              ([1, 1, 1, 1], [1, 1, 1, 1]),
              ([6, -2, 1, 5, -1], [-2, -1, 1, 5, 6]),
              ([6, 2, 11, 4, 5, 99, 22, 1], [1, 2, 4, 5, 6, 11, 22, 99])]

s = Sorting()


def test_bubble_sort():
    for i in test_cases:
        assert s.bubble_sort(i[0]) == i[1]


def test_heap_sort():
    for i in test_cases:
        assert s.heap_sort(i[0]) == i[1]


def test_quick_sort():
    for i in test_cases:
        assert s.quick_sort(i[0]) == i[1]


def test_merge_sort():
    for i in test_cases:
        assert s.merge_sort(i[0]) == i[1]
