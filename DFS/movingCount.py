class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = {}

        def DFS(i, j):
            if i >= m or j >= n or visited.get((i, j), 0): return 0
            visited[(i, j)] = 1
            count = 0
            while i:
                count += i % 10
                i //= 10
            while j:
                count += j % 10
                j //= 10
            if count > k: return 0
            return 1 + DFS(i + 1, j) + DFS(i, j + 1)

        return DFS(0, 0)


if __name__ == '__main__':
    m, n, k = 3, 2, 17
    test = Solution()
    print(test.movingCount(m, n, k))
