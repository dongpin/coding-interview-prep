# 5. Longest Palindromic Substring

def longest_palindrome(s):

    dp = [[0] * len(s) for _ in range(len(s))]
    result = ""

    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if i == j:
                dp[i][j] = 1
                result = s[i:j + 1] if j - i + 1 > len(result) else result
            elif i + 1 == j and s[i] == s[j]:
                dp[i][j] = 2
                result = s[i:j + 1] if j - i + 1 > len(result) else result
            elif s[i] == s[j] and dp[i + 1][j - 1] > 0:
                dp[i][j] = dp[i + 1][j - 1] + 2
                result = s[i:j + 1] if j - i + 1 > len(result) else result

    return result
