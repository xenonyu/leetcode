import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        stats = list(collections.Counter(nums).items())
        heap = [(0, 0)]

        def sift_up(heap, i):
            val = heap[i]
            while i >> 1 > 0 and val[1] < heap[i >> 1][1]:
                heap[i] = heap[i >> 1]
                i = i >> 1
            heap[i] = val

        def sift_down(heap, index, length):
            val = heap[index]
            while index << 1 < length:
                l, r = index << 1, index << 1 | 1
                small_child = r if r < length and heap[l][1] > heap[r][1] else l
                if heap[small_child][1] < val[1]:
                    heap[index] = heap[small_child]
                    index = small_child
                else:
                    break
            heap[index] = val

        for i in range(k):
            heap.append(stats[i])
            sift_up(heap, i + 1)
        # print(heap)

        for i in range(k, len(stats)):
            # print(heap)
            if stats[i][1] > heap[1][1]:
                heap[1] = stats[i]
                sift_down(heap, 1, k + 1)
        # print(heap)
        return [i[0] for i in heap[1:]]


if __name__ == '__main__':
    test = Solution()
    nums = [5, -3, 9, 1, 7, 7, 9, 10, 2, 2, 10, 10, 3, -1, 3, 7, -9, -1, 3, 3]
    k = 3
    res = test.topKFrequent(nums, k)
    print(res)
