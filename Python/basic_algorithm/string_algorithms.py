# Check if sting is palindromic
#

def is_palindromic(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))

# string sorts


def lsd_sort(s):
    pass


def msd_sort(s):
    pass


def three_way_quicksort(s):
    pass

# substring search


def kmp():
    pass


def boyer_moore():
    pass


def rabin_karp():
    pass

# regular expressions


def is_match(text, pattern):
    if not pattern:
        return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    if len(pattern) >= 2 and pattern[1] == '*':
        return is_match(text, pattern[2:]) or first_match and is_match(
            text[1:], pattern)
    else:
        return first_match and is_match(text[1:], pattern[1:])

# data compression

# Longest common subsequence


def longest_common_subsequence(xstr, ystr):
    if not xstr or not ystr:
        return ''
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return x + longest_common_subsequence(xs, ys)
    else:
        return max(longest_common_subsequence(xstr, ys),
                   longest_common_subsequence(xs, ystr), key=len)


def longest_common_subsequence_iterative(xstr, ystr):
    # Memorization or tabulation
    # This is tabulation approach
    xlen, ylen = len(xstr), len(ystr)
    tab = [[None for _ in range(ylen + 1)] for _ in range(xlen + 1)]
    for i in range(xlen + 1):
        for j in range(ylen + 1):
            if i == 0 or j == 0:
                tab[i][j] = ''
            elif xstr[i - 1] == ystr[j - 1]:
                tab[i][j] = tab[i - 1][j - 1] + xstr[i - 1]
            else:
                tab[i][j] = max(tab[i - 1][j], tab[i][j - 1], key=len)
    return tab[xlen][ylen]

# Longest increasing subsequence


def longest_increasing_subsequence(arr):
    if not arr:
        return []
    n = len(arr)
    dp = [1] * n
    parent = [-1] * n
    best = 0
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
        if dp[i] > dp[best]:
            best = i
    result = []
    i = best
    while i != -1:
        result.append(arr[i])
        i = parent[i]
    return result[::-1]

# Longest palindrome subsequence


def longest_palindrome_subsequence():
    pass

# Longest alternating subsequence


def longest_alternating_subsequence():
    pass

# Longest common substring


def longest_common_substring(xstr, ystr):
    pass


def longest_common_substring_iterative(xstr, ystr):
    lcs_res = [[0 for _ in range(len(ystr) + 1)] for _ in range(len(xstr) + 1)]

    result = 0
    for i in range(len(xstr) + 1):
        for j in range(len(ystr) + 1):
            if i == 0 or j == 0:
                lcs_res[i][j] = 0
            elif xstr[i - 1] == ystr[j - 1]:
                lcs_res[i][j] = lcs_res[i - 1][j - 1] + 1
                result = max(result, lcs_res[i][j])
            else:
                lcs_res[i][j] = 0
    return result

# Longest palindrome substring


def longest_palindrome_substring():
    pass

# Longest repeated substring


def longest_repeated_substring():
    pass

# Edit distance


def edit_distance(str1, str2):
    def edit_distance_helper(str1, str2, x, y):
        if x == 0:
            return y
        if y == 0:
            return x
        if str1[x - 1] == str2[y - 1]:
            return edit_distance_helper(str1, str2, x - 1, y - 1)
        return 1 + min(edit_distance_helper(str1, str2, x, y - 1),
                       edit_distance_helper(str1, str2, x - 1, y),
                       edit_distance_helper(str1, str2, x - 1, y - 1))
    return edit_distance_helper(str1, str2, len(str1), len(str2))
