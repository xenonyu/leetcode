from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        answer = []
        i = 0
        while i < len(nums) - 3:
            if i > 0 and nums[i] == nums[i - 1]:
                i = i + 1
                continue
            j = i + 1
            while j < len(nums) - 2:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j = j + 1
                    continue
                tempTarget = target - nums[i] - nums[j]
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    if nums[start] + nums[end] == tempTarget:
                        answer.append([nums[i], nums[j], nums[start], nums[end]])
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        start = start + 1
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1
                        end = end - 1
                    elif nums[start] + nums[end] < tempTarget:
                        start += 1
                    else:
                        end -= 1
                j += 1
            i +=1
        return answer


if __name__ == '__main__':
    test = Solution()
    inputList = [-3,-2,-1,0,0,1,2,3]
    target = 0
    result = test.fourSum(inputList, target)
    print(result)