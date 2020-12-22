class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if not haystack: return -1
        slow, fast = 0, 0
        while fast < len(haystack):
            if haystack[fast] == needle[fast - slow]:
                if fast - slow == len(needle) - 1: return slow
                fast += 1
                continue
            slow = slow + 1
            fast = slow
        return -1

    def strStrKMP(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if len(haystack) < len(needle): return -1
        dp = [[0 for i in range(256)] for j in range(len(needle))]
        dp[0][ord(needle[0])] = 1

        def buildKMP(needle):
            X = 0
            for i in range(1, len(needle)):
                for j in range(256):
                    if ord(needle[i]) == j:
                        dp[i][j] = i + 1
                    else:
                        dp[i][j] = dp[X][j]
                print(ord(needle[i]))
                X = dp[X][ord(needle[i])]

        def search(haystack, needle):
            j = 0
            for i in range(len(haystack)):
                j = dp[j][ord(haystack[i])]
                if j == len(needle): return i - j + 1
            return -1

        buildKMP(needle)
        return search(haystack, needle)


if __name__ == '__main__':
    test = Solution()
    haystack = "hello"
    needle = "ll"
    res = test.strStrKMP(haystack, needle)
    print(res)
