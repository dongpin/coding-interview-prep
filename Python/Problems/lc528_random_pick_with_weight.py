
import random
'''
def generate_random_number(values, probabilities):
    prefix_sum_of_probabilities = list(itertools.accumulate(probabilities))
    pass
'''


class RandomGenerator:
    def __init__(self, w):
        self.cum = [0] * len(w)
        for idx, ele in enumerate(w):
            self.cum[idx] = ele if idx == 0 else ele + self.cum[idx - 1]

    def pickIndex(self):
        rn = random.randint(1, self.cum[-1])
        return self.nearest(rn)

    def nearest(self, rn):
        lo, hi = 0, len(self.cum) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.cum[mid] == rn:
                return mid
            elif self.cum[mid] < rn:  # if this is true, in this question, mid+1 also exist
                if rn <= self.cum[mid + 1]:
                    return mid + 1
                lo = mid + 1
            else:
                if mid == 0:
                    return mid
                hi = mid - 1


if __name__ == "__main__":
    gen = RandomGenerator([5, 1, 1])
    for _ in range(20):
        print(gen.pickIndex())
