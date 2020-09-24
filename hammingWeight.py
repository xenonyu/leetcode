class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n = n >> 1
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.hammingWeight(9))
    print(-1 & 0xffffffff)
