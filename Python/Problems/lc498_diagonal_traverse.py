# 498. Diagonal Traverse

from collections import defaultdict


def diagonal_traverse(matrix):
    if not matrix:
        return []
    seq = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            seq[i + j].append(matrix[i][j])

    result = []
    dir = -1
    for i in range(len(matrix) + len(matrix[0]) - 1):
        result.extend(seq[i][::dir])
        dir *= -1
    return result


def diagonal_traverse_less_space(matrix):
    r, c = len(matrix), len(matrix[0])
    result = []
    for i in range(r + c - 1):
        if i % 2 == 0:
            for j in range(max(0, i - r + 1), min(c, i + 1)):
                # from low to high
                result.append(matrix[i - j][j])
        else:
            for j in range(max(0, i - c + 1), min(r, i + 1)):
                result.append(matrix[j][i - j])
    return result
