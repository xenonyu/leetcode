class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.sLen, self.pLen = len(s), len(p)
        memo = {}

        def dp(i, j):
            # base case
            # print(i, j)
            if j == self.pLen: return i == self.sLen
            if i == self.sLen:
                if (self.pLen - j) % 2: return False
                for k in range(j + 1, self.pLen, 2):
                    if p[k] != "*": return False
                return True
            key = (i, j)
            if key in memo: return memo[key]
            if s[i] == p[j] or p[j] == '.':
                if j < self.pLen - 1 and p[j + 1] == '*':
                    memo[key] = (dp(i + 1, j) or dp(i, j + 2))
                else:
                    memo[key] = dp(i + 1, j + 1)
            else:
                if j < self.pLen - 1 and p[j + 1] == '*':
                    memo[key] = dp(i, j + 2)
                else:
                    memo[key] = False
            return memo[key]

        return dp(0, 0)


if __name__ == '__main__':
    s = 'a'
    p = ".*..a*"
    test = Solution()
    print(test.isMatch(s, p))
