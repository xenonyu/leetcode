from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.res = 0
        n = len(nums)

        def backTrack(index, target):
            if index == n:
                if target == 0: self.res += 1
                return
            target -= nums[index]
            backTrack(index + 1, target)
            target += nums[index]
            target += nums[index]
            backTrack(index + 1, target)
            target -= nums[index]

        backTrack(0, S)
        return self.res


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    target = 3
    test = Solution()
    print(test.findTargetSumWays(nums, target))
