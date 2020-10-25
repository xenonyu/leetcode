class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '11'
        preRes = self.countAndSay(n - 1)
        pre, res, count = preRes[0], '', 1
        for i in range(1, len(preRes)):
            if preRes[i] == pre:
                count += 1
            else:
                res += str(count) + pre
                pre = preRes[i]
                count = 1
        res += str(count) + preRes[-1]
        return res


if __name__ == '__main__':
    n = 3
    test = Solution()
    print(test.countAndSay(n))
