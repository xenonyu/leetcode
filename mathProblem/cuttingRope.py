class Solution:
    def __init__(self):
        self.MOD = 1000000007

    def myPow(self, x: int, n: int) -> int:
        res = 1
        while n:
            n, r = divmod(n, 2)
            if r:
                res *= x % self.MOD
            x *= x % self.MOD
        return res

    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        q, r = divmod(n, 3)
        res = 1
        x = 3
        if r == 0:
            return self.myPow(3, q)
        elif r == 1:
            return self.myPow(3, q - 1) * 4
        else:
            return self.myPow(3, q) * 2


if __name__ == '__main__':
    test = Solution()
    print(test.cuttingRope(120))
