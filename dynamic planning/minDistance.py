class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def recur(word1: str, word2: str) -> int:
            if word1 + ";" + word2 in memo: return memo[word1 + ";" + word2]
            if not word1:
                return len(word2)
            elif not word2:
                return len(word1)
            elif word1[0] == word2[0]:
                res = recur(word1[1:], word2[1:])
                print(word1 + ";" + word2)
                memo[word1 + ";" + word2] = res
                return res
            else:
                # 删除word1
                res1 = 1 + recur(word1[1:], word2)
                # 增加word1
                res2 = 1 + recur(word1, word2[1:])
                res3 = 1 + recur(word1[1:], word2[1:])
                res = min(res1, res2, res3)
                memo[word1 + ";" + word2] = res
                return res

        return recur(word1, word2)

    def minDistanceII(self, word1: str, word2: str) -> int:
        word1Len, word2Len = len(word1), len(word2)
        dp = [[0 for _ in range(word1Len + 1)] for _ in range(word2Len + 1)]
        for i in range(word1Len + 1): dp[0][i] = i
        for j in range(word2Len + 1): dp[j][0] = j
        for j in range(1, word2Len + 1):
            for i in range(1, word1Len + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1]
                else:
                    dp[j][i] = 1 + min(
                        dp[j - 1][i - 1],
                        dp[j][i - 1],
                        dp[j - 1][i]
                    )
        return dp[-1][-1]


if __name__ == '__main__':
    word1 = "sea"
    word2 = "eat"
    test = Solution()
    print(test.minDistanceII(word1, word2))
