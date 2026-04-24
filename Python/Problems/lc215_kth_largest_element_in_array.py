# 215. Kth Largest Element in an Array

import heapq


def find_kth_largest(nums, k):
    pq = list(nums[:k])
    heapq.heapify(pq)

    for i in range(k, len(nums)):
        if pq[0] < nums[i]:
            heapq.heappushpop(pq, nums[i])
    return pq[0]
