from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if not length: return 0
        i = 0
        for j in range(1, length):
            if nums[i] != nums[j]:
                nums[i] = nums[j]
                i += 1
        return i + 1


if __name__ == '__main__':
    test = Solution()
    inputList = [1, 1, 2, 1, 2, 1, 2]
    length = test.removeDuplicates(inputList)
    for i in range(length):
        print(inputList[i])
