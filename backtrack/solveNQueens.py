from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        dp = [['.'] * n for _ in range(n)]

        def isValid(dp, row, col):
            for i in range(row):
                if dp[i][col] == 'Q': return False
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if dp[i][j] == 'Q': return False
                i -= 1
                j += 1
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if dp[i][j] == 'Q': return False
                i -= 1
                j -= 1
            return True

        def backTrack(dp, row):
            if row == n:
                res.append([''.join(row) for row in dp])
                return
            for col in range(n):
                if not isValid(dp, row, col): continue
                dp[row][col] = 'Q'
                backTrack(dp, row + 1)
                dp[row][col] = '.'

        backTrack(dp, 0)
        return res


if __name__ == '__main__':
    n = 4
    test = Solution()
    print(test.solveNQueens(4))
