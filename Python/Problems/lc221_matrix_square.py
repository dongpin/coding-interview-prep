# 221. Maximal Square

def find_max_square(matrix):
    if not matrix:
        return 0

    result = 0
    dp = [[0 for _ in range(len(matrix[0]) + 1)]
          for _ in range(len(matrix) + 1)]
    for i in range(1, len(matrix) + 1):
        for j in range(1, len(matrix[0]) + 1):
            if matrix[i - 1][j - 1] == '1':
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1]
                               [j], dp[i][j - 1]) + 1
                result = max(result, dp[i][j])
    return result ** 2
