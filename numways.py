class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n - 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    test = Solution()
    ans = test.numWays(7)
    print(ans)
