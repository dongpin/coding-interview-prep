# 85. Maximal Rectangle

def find_max_rectangle(matrix):
    if not matrix:
        return 0

    def largest_rectangle(heights):

        result = 0

        # append dummy build in the end
        # in order to pop up all building in the end
        heights.append(0)
        # append dummy build in stack in order to facilitate comparison
        stack = [-1]
        for i in range(len(heights)):
            # find desceding order
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                # remove 2 edges
                w = i - stack[-1] - 1
                result = max(result, h * w)
            stack.append(i)
        heights.pop()
        return result

    max_area = 0
    dp = [0] * len(matrix[0])
    for i in range(len(matrix)):
        # update the height in the row
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                dp[j] += 1
            else:
                dp[j] = 0
        max_area = max(max_area, largest_rectangle(dp))
    return max_area
