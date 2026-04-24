# 633. Sum of Square Numbers

from math import sqrt


def judge(c):
    i, j = 0, int(sqrt(c))
    while i <= j:
        pow_sum = i * i + j * j
        if pow_sum == c:
            return True
        elif pow_sum < c:
            i += 1
        else:
            j -= 1
    return False
