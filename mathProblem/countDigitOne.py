class Solution:
    def countDigitOne(self, n: int) -> int:
        high, low, cur, res, digit = n // 10, 0, n % 10, 0, 1
        while cur or high:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit
            digit *= 10
            cur = high % 10
            high //= 10
        return res


if __name__ == '__main__':
    test = Solution()
    result = test.countDigitOne(12)
    print(result)
