import collections

from handleInput import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h, w = len(grid), len(grid[0])
        direction = [(0, -1), (-1, 0)]
        landMap = {}
        if grid[0][0] == '1': landMap[(0, 0)] = (0, 0)
        for i in range(1, h):
            if grid[i][0] == '1':
                if grid[i - 1][0] == '1':
                    landMap[(i, 0)] = (i - 1, 0)
                else:
                    landMap[(i, 0)] = (i, 0)
        for j in range(1, w):
            if grid[0][j] == '1':
                if grid[0][j - 1] == '1':
                    landMap[(0, j)] = (0, j - 1)
                else:
                    landMap[(0, j)] = (0, j)

        def find(i, j):
            if landMap[(i, j)] == (i, j):
                return i, j
            else:
                return find(*landMap[(i, j)])

        def union(x, y):
            rootx = find(*x)
            rooty = find(*y)
            landMap[rooty] = rootx

        for i in range(1, h):
            for j in range(1, w):
                if grid[i][j] == '1':
                    landMap[(i, j)] = (i, j)
                    if grid[i - 1][j] == '1' and grid[i][j - 1] == '1':
                        union((i - 1, j), (i, j - 1))
                        landMap[(i, j)] = (i - 1, j)
                    elif grid[i - 1][j] == '1':
                        landMap[(i, j)] = (i - 1, j)
                    elif grid[i][j - 1] == '1':
                        landMap[(i, j)] = (i, j - 1)

        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    landMap[(i, j)] = find(i, j)
        return len(set(landMap.values()))

    def numIslandsII(self, grid: List[List[str]]):
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"

        return num_islands

    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        h = len(grid)
        w = len(grid[0])

        def DFS(i, j):
            grid[i][j] = '0'
            for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < h and 0 <= y < w and grid[x][y] == '1':
                    DFS(x, y)

        res = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    res += 1
                    DFS(i, j)
        return res


if __name__ == '__main__':
    inputGrid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
    test = Solution()
    print(test.numIslandsII(inputGrid))
