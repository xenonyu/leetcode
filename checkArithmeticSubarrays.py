from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for left, right in zip(l, r):
            targetNums = nums[left:right + 1]
            targetNums.sort()
            if len(targetNums) < 3:
                res.append(True)
                continue
            d, flag = targetNums[1] - targetNums[0], True
            for i in range(2, len(targetNums)):
                if targetNums[i] - targetNums[i - 1] != d:
                    flag = False
                    break
            if flag:
                res.append(True)
            else:
                res.append(False)
        return res


if __name__ == '__main__':
    test = Solution()
    nums, l, r = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10], [0, 1, 6, 4, 8, 7], [4, 4, 9, 7, 9, 10]
    res = test.checkArithmeticSubarrays(nums, l, r)
    print(res)
