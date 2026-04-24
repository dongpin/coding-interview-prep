

class Sorting:
    """
    Class for sorting algorithms
    """

    def __init__(self):
        pass

    def bubble_sort(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def selection_sort(self, arr):
        pass

    def insertion_sort(self, arr):
        pass

    def shell_sort(self, arr):
        pass

    def counting_sort(self, arr):
        pass

    def radix_sort(self, arr):
        pass

    def bucket_sort(self, arr):
        pass

    def _merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        i, j = 0, 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1
        return res

    def merge_sort(self, arr):
        if not arr:
            return []
        elif len(arr) == 1:
            return arr
        else:
            m = len(arr) // 2
            left = self.merge_sort(arr[:m])
            right = self.merge_sort(arr[m:])
            return self._merge(left, right)

    def quick_sort(self, arr):
        if not arr:
            return []
        else:
            p = arr[0]
            lesser = self.quick_sort([x for x in arr[1:] if x <= p])
            greater = self.quick_sort([x for x in arr[1:] if x > p])
            return lesser + [p] + greater

    def _heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[i]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        # swap largest to root and heapify the largest element
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._heapify(arr, n, largest)

    # Time complexity O(nlogn) for all cases
    def heap_sort(self, arr):
        n = len(arr)
        # build max heap
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)

        # move the largest one to end of arr (sorted part)
        # heapify the unsorted part
        for i in range(n - 1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self._heapify(arr, i, 0)

        return arr
