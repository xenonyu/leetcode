from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num in dic:
                return num
            dic[num] = num


if __name__ == '__main__':
    test = Solution()
    inputList = [3, 1, 2, 3]
    res = test.findRepeatNumber(inputList)
    print(res)