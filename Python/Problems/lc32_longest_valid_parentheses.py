# 32. Longest Valid Parentheses

def find_longest_valid_parenthese(s):
    """
    :type s: str
    :rtype: int
    """

    result = 0
    stack = []
    for i, v in enumerate(s):
        if v == '(':
            stack.append(i)
        else:
            if stack and s[stack[-1]] == '(':
                stack.pop()
                if stack:
                    result = max(result, i - stack[-1])
                else:
                    result = max(result, i + 1)
            else:
                stack.append(i)

    return result
