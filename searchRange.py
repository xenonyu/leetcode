from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                ans = [mid, mid]
                while ans[0] - 1 >= 0 and nums[ans[0] - 1] == target: ans[0] -= 1
                while ans[0] + 1 <= len(nums) - 1 and nums[ans[1] + 1] == target: ans[1] += 1
                return ans
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [-1, -1]


if __name__ == '__main__':
    test = Solution()
    inputList = [5, 7, 7, 8, 8, 10]
    target = 8
    print(test.searchRange(inputList, target))
