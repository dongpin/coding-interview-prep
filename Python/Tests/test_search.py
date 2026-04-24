from python.basic_algorithm.search import binary_search, linear_search, ternary_search

test_cases = [([1, 3, 5, 7, 9, 12, 24], 7, 3),
              ([1], 1, 0),
              ([], 1, -1),
              ([1, 2], 3, -1),
              ([2, 4, 6, 9, 9, 9, 10], 10, 6)]


def test_linear_search():
    for t in test_cases:
        assert linear_search(t[0], t[1]) == t[2]


def test_binary_search():
    for t in test_cases:
        assert binary_search(t[0], t[1]) == t[2]


def test_ternary_search():
    for t in test_cases:
        assert ternary_search(t[0], t[1]) == t[2]
