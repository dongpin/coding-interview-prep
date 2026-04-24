# 168. Excel Sheet Column Title


def num_to_title(n):
    result = []
    while n > 0:
        result.append(chr(ord('A') + ((n - 1) % 26)))
        n = (n - 1) // 26
    return ''.join(result[::-1])
