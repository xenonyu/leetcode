import functools
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        strs = [str(i) for i in nums]

        def fast_sort(low: int, high: int):
            if low >= high: return
            i, j = low, high
            while i < j:
                while sortRule(strs[j], strs[low]) == 1 and i < j: j -= 1
                while sortRule(strs[low], strs[i]) == 1 and i < j: i += 1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[low] = strs[low], strs[i]
            fast_sort(low, i - 1)
            fast_sort(i + 1, high)

        def sortRule(x, y):
            if x + y < y + x:
                return -1
            else:
                return 1

        strs.sort(key=functools.cmp_to_key(sortRule))
        fast_sort(0, len(strs) - 1)
        return "".join(strs)


if __name__ == '__main__':
    test = Solution()
    print(test.minNumber([3, 30, 34, 5, 9]))
