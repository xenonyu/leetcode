from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 1: return nums
        pre, last = 0, len(nums) - 1
        while pre < last:
            while pre < last and nums[pre] % 2 == 1: pre += 1
            while pre < last and nums[last] % 2 == 0: last -= 1
            nums[pre], nums[last] = nums[last], nums[pre]
        return nums


if __name__ == '__main__':
    inputList = [1, 2, 3, 4]
    test = Solution()
    ans = test.exchange(inputList)
    print(ans)
