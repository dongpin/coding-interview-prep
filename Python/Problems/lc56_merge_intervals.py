# 56. Merge Intervals

def merge(intervals):

    if not intervals or len(intervals) < 2:
        return intervals

    result = []
    intervals = sorted(intervals, key=lambda k: k[0])
    start, end = intervals[0][0], intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= end:
            end = max(end, intervals[i][1])
        else:
            result.append([start, end])
            start, end = intervals[i][0], intervals[i][1]
    result.append([start, end])
    return result
