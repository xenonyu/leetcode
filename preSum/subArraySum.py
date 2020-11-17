from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = {0: 1}
        res, prefix = 0, 0
        for index, val in enumerate(nums):
            prefix += val
            target = prefix - k
            res += preSum.get(target, 0)
            preSum[prefix] = preSum.get(prefix, 0) + 1
        return res
