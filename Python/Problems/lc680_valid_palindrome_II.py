# 680. Valid Palindrome II

def valid_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    def parlindrome(s):
        return all(s[i] == s[~i] for i in range(len(s) // 2))

    for i in range(len(s) // 2):
        if s[i] != s[~i]:
            j = len(s) - i
            return parlindrome(s[i + 1:j]) or parlindrome(s[i:j - 1])
    return True
