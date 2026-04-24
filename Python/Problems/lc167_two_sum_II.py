# 167. Two Sum II

def two_sum(nums, target):
    if not nums:
        return None

    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            return [i, j]
        elif s < target:
            i += 1
        else:
            j -= 1
    return None
