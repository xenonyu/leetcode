from typing import List


def minimumOperations(leaves: str) -> int:
    i = 1
    j = len(leaves) - 1
    ans = []
    while i < j:
        count = 0
        for t in range(0, i):
            if leaves[i] == "y":
                count += 1
        for t in range(i, j):
            if leaves[t] == "r":
                count += 1
        for t in range(j, len(leaves)):
            if leaves[t] == "y":
                count += 1
        ans.append(count)

    return min(ans)


print(minimumOperations("rrryyyrryyyrr"))


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])
        for i in range(1, len(nums)):
            dp.append(nums[i] + max(dp[i - 1], 0))
        return max(dp)


if __name__ == "__main__":
    test = Solution()
    inputList = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(test.maxSubArray(inputList))
