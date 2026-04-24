import random

from python.basic_algorithm.dc_closest_pairs import (
    closest_pair_brute_force,
    closest_pair_divide_and_conquer,
)


def test_closest_pair_1D():
    data = [100 * random.random() for i in range(10)]
    assert closest_pair_brute_force(data) == closest_pair_divide_and_conquer(data)
