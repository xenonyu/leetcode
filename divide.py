class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        isPositive = True if dividend * divisor > 0 else False
        dividend = dividend if dividend >= 0 else -dividend
        divisor = divisor if divisor >= 0 else -divisor
        if divisor > dividend: return 0

        def recur(dd) -> int:
            ans = 1
            if divisor > dd: return 0
            if divisor == dd: return 1
            while dd > ans * 2 * divisor:
                ans *= 2
            ans += recur(dd - ans * divisor)
            return ans

        ans = recur(dividend)
        ans = ans - 1 if ans > 2 ** 31 - 1 else ans

        return ans if isPositive else -ans


if __name__ == '__main__':
    test = Solution()
    res = test.divide(-2147483648, -1)
    print(res)
