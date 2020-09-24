class Solution:
    def findNthDigit(self, n: int) -> int:
        start, count, digit = 1, 9, 1
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit
        bit = (n - 1) % digit + 1
        # print(num, digit, bit)
        return num // (10 ** (digit - bit)) % 10


if __name__ == '__main__':
    test = Solution()
    result = test.findNthDigit(1111)
    print(result)
    print()
