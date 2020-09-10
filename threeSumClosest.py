from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        best = 10 ** 7
        def getDistance(a, b):
            return abs(a - b)
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start = i + 1
            end = length - 1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum == target:
                    return target
                elif sum < target:
                    start += 1
                else:
                    end -= 1
                if getDistance(best, target) > getDistance(sum, target):
                    best = sum
        return best


if __name__ == '__main__':
    test = Solution()
    inputArray = [-1, 2, 1, -4]
    target = 1
    print(test.threeSumClosest(nums=inputArray, target=target))