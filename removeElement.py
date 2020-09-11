from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        if not length:
            return 0
        slow = 0
        for fast in range(length):
            if nums[fast] == val:
                continue
            nums[slow] = nums[fast]
            slow += 1
        return slow


if __name__ == '__main__':
    test = Solution()
    inputList = [3, 2, 2, 3]
    val = 2
    length = test.removeElement(inputList, val)
    for i in range(length):
        print(inputList[i])
