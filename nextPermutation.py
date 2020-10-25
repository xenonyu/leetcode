from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length - 2, -1, -1):
            index = length - 1
            while index > i:
                if nums[i] < nums[index]:
                    nums[index], nums[i] = nums[i], nums[index]
                    nums[i + 1:] = nums[i + 1:] = nums[len(nums) - 1:i:-1]
                    return
                else:
                    index -= 1
        else:
            nums.reverse()


if __name__ == '__main__':
    inputList = [3, 2, 1]
    test = Solution()
    test.nextPermutation(inputList)
