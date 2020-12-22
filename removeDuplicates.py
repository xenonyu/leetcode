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

    def removeDuplicatesII(self, nums: List[int]) -> int:
        slow, fast, n = 1, 1, len(nums)
        count = 2
        while fast < n:
            if nums[fast] == nums[fast - 1]:
                count -= 1
            else:
                count = 1
            if count > 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


if __name__ == '__main__':
    # test = Solution()
    # inputList = [1, 1, 1, 2, 1, 2, 1, 2]
    # length = test.removeDuplicatesII(inputList)
    # print(inputList[:length])
    print(-1 ^ (-1) < 0)
