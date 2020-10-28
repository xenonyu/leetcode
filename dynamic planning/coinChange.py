from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return -1 if dp[amount] == amount + 1 else dp[amount]

    def coinChangeUpDown(self, coins: List[int], amount: int) -> int:
        memo = dict()

        def dp(amount):
            if amount in memo: return memo[amount]
            if amount == 0: return 0
            if amount < 0: return -1
            least = amount + 1
            for i in coins:
                subProblem = dp(amount - i)
                if subProblem == -1: continue
                least = min(least, 1 + subProblem)
            memo[amount] = least if least != amount + 1 else -1
            return memo[amount]

        return dp(amount)
