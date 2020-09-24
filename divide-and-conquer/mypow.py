class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 分治
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            n, remainder = divmod(n, 2)
            if remainder:
                res *= x
            x = x * x
        return res
        # 快速幂
        # res = 1
        # if n < 0: x, n = 1 / x, -n
        # while n:
        #     if n & 1: res *= x
        #     x = x * x
        #     n = n >> 1
        # return res


if __name__ == "__main__":
    test = Solution()
    ans = test.myPow(2, 3)
    print(ans)
    print((1 << 1) ^ 3)
