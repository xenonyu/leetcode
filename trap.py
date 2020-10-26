from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        leftMaxs, rightMaxs = [], []
        leftMax, rightMax = -float('inf'), -float('inf')
        res = 0
        for i in range(len(height)):
            leftMax = max(height[i], leftMax)
            leftMaxs.append(leftMax)
        for i in range(len(height) - 1, -1, -1):
            rightMax = max(height[i], rightMax)
            rightMaxs.insert(0, rightMax)
        for i in range(1, len(height) - 1):
            maxAround = min(leftMaxs[i - 1], rightMaxs[i + 1])
            if maxAround > height[i]:
                res += maxAround - height[i]
        return res


if __name__ == '__main__':
    inputList = [4, 2, 0, 3, 2, 5]
    test = Solution()
    res = test.trap(inputList)
    print(res)
