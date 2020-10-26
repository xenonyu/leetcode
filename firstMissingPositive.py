from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            # nums[i] should be i + 1
            if nums[i] != i + 1 and 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                i -= 1
            i += 1
        for i, num in enumerate(nums):
            if i + 1 != num: return i + 1
        return len(nums) + 1

    def firstMissingPositiveII(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0: nums[i] = n + 1
        for i in range(n):
            target = abs(nums[i])
            if target - 1 < n and nums[target - 1] > 0: nums[target - 1] = -nums[target - 1]
        for i in range(n):
            if nums[i] > 0: return i + 1
        return n + 1

    def firstMissingPositiveIII(self, nums: List[int]) -> int:
        b = 0

        for i in nums:
            if 0 < i <= len(nums):
                b |= 1 << i

        offset = 1
        while True:
            t = 1 << offset
            if not (b & t) == t:
                return offset
            offset += 1


if __name__ == '__main__':
    test = Solution()
    inputList = [1, 3, 5]
    res = test.firstMissingPositiveIII(inputList)
    print(res)
