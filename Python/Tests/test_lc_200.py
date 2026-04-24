from python.problems.lc205_isomorphic_str import is_isomorphic
from python.problems.lc215_kth_largest_element_in_array import find_kth_largest
from python.problems.lc289_game_of_life import game_of_life


def test_is_isomorphic():
    assert is_isomorphic("egg", "add")
    assert not is_isomorphic("foo", "bar")
    assert is_isomorphic("paper", "title")


def test_find_kth_largest():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 3) == 4


def test_game_of_life():
    matrix = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    game_of_life(matrix)
    assert matrix == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
