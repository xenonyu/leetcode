from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l


if __name__ == '__main__':
    inputList = [1, 3, 5, 6]
    target = 4
    test = Solution()
    print(test.searchInsert(inputList, target))
