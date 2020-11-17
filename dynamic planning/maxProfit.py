from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp = [[[-float('inf'), -float('inf')], [-float('inf'), -float('inf')], [-float('inf'), -float('inf')],
               [-float('inf'), -float('inf')]] for _ in range(length)]
        dp[0][2][0] = 0
        dp[0][1][1] = -prices[0]
        print(dp)
        for i in range(1, length):
            for k in range(3):
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k + 1][0] - prices[i])
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
        for i in dp:
            print(i)
        return int(max(dp[length - 1][0][0], dp[length - 1][1][0], dp[length - 1][2][0]))

    def maxProfitII(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        left, right = [], []
        minp = float('inf')
        maxleft = 0
        for i in prices:
            if i < minp:
                minp = i
            if i - minp > maxleft:
                maxleft = i - minp
            left += [maxleft]

        maxp = float('-inf')
        maxright = 0
        for i in prices[::-1]:
            if i > maxp:
                maxp = i
            if maxp - i > maxright:
                maxright = maxp - i
            right += [maxright]

        res = max(i + j for i, j in zip(left, right[-2::-1]))
        return max(res, left[-1])

if __name__ == '__main__':
    test = Solution()
    inputList = [3, 3, 5, 0, 0, 3, 1, 4]
    print(test.maxProfitII(inputList))
