class Solution:
    def totalNQueens(self, n: int) -> int:
        visited = {}

        def backTrack(layer):
            if layer == n: return 1
            res = 0
            for i in range(n):
                if not isValid(layer, i): continue
                visited[(layer, i)] = 1
                res += backTrack(layer + 1)
                del visited[(layer, i)]
            return res

        def isValid(layer, index):
            for i in range(1, min(layer, index) + 1):
                if visited.get((layer - i, index - i), 0): return False
            for i in range(1, min(n - index - 1, layer) + 1):
                if visited.get((layer - i, index + i), 0): return False
            for i in range(layer):
                if visited.get((i, index), 0): return False
            return True

        res = backTrack(0)
        return res


if __name__ == '__main__':
    n = 4
    test = Solution()
    print(test.totalNQueens(n))
