"""
    Compute nearest pair of points using two algorithms
    https://rosettacode.org/wiki/Closest-pair_problem#Python
"""
import math
import random
from operator import itemgetter

# 1D senario


def closest_pair_brute_force(points):
    current_min = (float('inf'), (None, None))
    sorted_points = sorted(points)
    for i in range(len(sorted_points) - 1):
        current_min = min(current_min,
                          (abs(sorted_points[i] - sorted_points[i + 1]),
                           (sorted_points[i],
                            sorted_points[i + 1])),
                          key=itemgetter(0))
    return current_min


def closest_pair_divide_and_conquer(points):
    sorted_points = sorted(points)
    return closest_pairs_divide(sorted_points)


def closest_pairs_divide(points):
    num_points = len(points)
    if num_points < 2:
        return (float('inf'), (None, None))
    elif num_points == 2:
        return (abs(points[0] - points[1]), (points[0], points[1]))
    else:
        m = num_points // 2
        left = points[:m]
        right = points[m:]
        left_min = closest_pairs_divide(left)
        right_min = closest_pairs_divide(right)
        min_so_far = min(left_min, right_min, key=itemgetter(0))
        return closest_pair_combine(left, right, min_so_far)


def closest_pair_combine(left, right, min_so_far):
    lower = left[-1] - min_so_far[0]
    upper = right[-1] + min_so_far[0]
    for i in range(len(left)):
        if lower <= left[i] <= upper and lower <= right[0] <= upper:
            min_so_far = min(
                min_so_far,
                (abs(
                    left[i] -
                    right[0]),
                    (left[i],
                     right[0])),
                key=itemgetter(0))
    return min_so_far

# 2D senario


def distance(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


def closest_pair_2d_brute_force(points):
    num_points = len(points)
    if num_points < 2:
        return None, (None, None)
    return min(((distance(points[i], points[j]), points[i], points[j])
                for i in range(num_points - 1) for j in range(i + 1, num_points)),
               key=itemgetter(0))


def closest_pair_2d_divide_and_conquer(points):
    if len(points) < 2:
        return None

    sorted_points = sorted(points, key=itemgetter(0))
    return closest_pairs_2d_divide(sorted_points)


def closest_pairs_2d_divide(points):
    num_points = len(points)
    if num_points < 2:
        return float('inf'), None, None
    elif num_points == 2:
        return (distance(points[0], points[1]), points[0], points[1])
    else:
        m = num_points // 2
        left = points[:m]
        right = points[m:]
        left_min = closest_pairs_2d_divide(left)
        right_min = closest_pairs_2d_divide(right)
        min_so_far = min(left_min, right_min, key=itemgetter(0))
        return closest_pair_2d_combine(left, right, min_so_far)


def closest_pair_2d_combine(left, right, min_so_far):
    lower = left[-1][0] - min_so_far[0]
    upper = left[-1][0] + min_so_far[0]
    current_min = min_so_far
    for i in range(len(left)):
        if lower <= left[i][0] <= upper:
            for j in range(min(len(right), 7)):
                if lower <= right[j][0] <= upper \
                        and abs(left[i][1] - right[j][1]) < min_so_far[0]:
                    current_min = min(
                        current_min,
                        (distance(
                            left[i],
                            right[j]),
                            left[i],
                            right[j]),
                        key=itemgetter(0))
    return min(min_so_far, current_min, key=itemgetter(0))


if __name__ == '__main__':
    data = [100 * random.random() for i in range(10)]
    print('Closest pair - 1D:')
    print(data)
    print(closest_pair_brute_force(data))
    print(closest_pair_divide_and_conquer(data))
    print()
    print('Closest pair - 2D:')
    data_2d = [(100 * random.random(), 100 * random.random())
               for i in range(10)]
    print(data_2d)
    print(closest_pair_2d_brute_force(data_2d))
    print(closest_pair_2d_divide_and_conquer(data_2d))
