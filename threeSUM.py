from typing import List
import numpy as np

class Solution:
    def twoSum(self, nums, start, end, target):
        result = []
        while start < end:
            sum = nums[start] + nums[end]
            if sum == target:
                result.append([nums[start], nums[end], -target])
                while start < end and nums[start] == nums[start + 1]:
                    start = start + 1
                start = start + 1
                while start < end and nums[end] == nums[end - 1]:
                    end = end - 1
                end = end - 1
            elif sum < target:
                start = start + 1
            else:
                end = end - 1
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            result = self.twoSum(nums=nums, start=i+1, end=len(nums)-1, target=-nums[i])
            answer.extend(result)

        return answer


if __name__ == '__main__':
    inputList = [0, 0, 0, 0]
    test = Solution()
    print(test.threeSum(inputList))
