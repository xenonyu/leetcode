from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        """

        :rtype: object
        """
        i = 0
        repeat = set()
        ma, mi = 0, 14
        for i in range(5):
            if not nums[i]: continue
            ma = max(ma, nums[i])
            mi = min(mi, nums[i])
            if nums[i] in repeat: return False
            repeat.add(nums[i])
        return True if ma - mi < 5 else False


if __name__ == '__main__':
    test = Solution()
    inputList = [1, 2, 3, 4, 5]
    res = test.isStraight(inputList)
    print(res)
