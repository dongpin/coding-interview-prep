# 3. Longest Substring Without Repeating Characters


def longest_substring_without_repeating_chars(s):

    result = 0
    chars = set()
    i, j = 0, 0
    while i < len(s) and j < len(s):
        if s[j] not in chars:
            chars.add(s[j])
            j += 1
            result = max(result, j - i)
        else:
            chars.remove(s[i])
            i += 1
    return result
