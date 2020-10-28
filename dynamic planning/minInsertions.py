class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        memo = [[-1] * n for _ in range(n)]
        for i in range(n): memo[i][i] = 0

        def dp(begin, end):
            if begin > end: return 0
            if memo[begin][end] != -1: return memo[begin][end]
            if s[begin] == s[end]:
                memo[begin][end] = dp(begin + 1, end - 1)
                return memo[begin][end]
            else:
                left = dp(begin, end - 1) + 1
                right = dp(begin + 1, end) + 1
                memo[begin][end] = min(left, right)
                return memo[begin][end]

        return dp(0, n - 1)

    def minInsertionsDownUP(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j] + 1, dp[i][j - 1] + 1)
        return dp[0][n - 1]
