from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [-1, -1]

        def leftBound(l, r, target):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1 if l == len(nums) or nums[l] != target else l

        def rightBound(l, r, target):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1 if r < 0 or nums[r] != target else r

        res[0] = leftBound(l, r, target)
        res[1] = rightBound(l, r, target)
        return res


if __name__ == '__main__':
    test = Solution()
    inputList = [5, 7, 7, 8, 8, 10]
    target = 8
    print(test.searchRange(inputList, target))
