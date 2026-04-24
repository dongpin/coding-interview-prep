# 84. Largest Rectangle in Histogram

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
