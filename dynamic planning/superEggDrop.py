class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()

        def dp(N, K):
            if K == 1: return N
            if N == 0: return 0
            if (N, K) in memo: return memo[(N, K)]
            res = N
            for i in range(1, N + 1):
                res = min(res, max(dp(i - 1, K - 1), dp(N - i + 1, K)) + 1)
            memo[(N, K)] = res
            return res

        return dp(N, K)


if __name__ == '__main__':
    K = 2
    N = 6
    test = Solution()
    print(test.superEggDrop(K, N))
