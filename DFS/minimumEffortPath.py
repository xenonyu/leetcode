import collections

from handleInput import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        visited = collections.defaultdict()
        row, col = len(heights), len(heights[0])

        def DFS(i, j, last):
            if i < 0 or i >= row or j < 0 or j >= col: return float('inf')
            # print(i, j, m)
            if not visited.get((i, j), 0):
                visited[(i, j)] = 1
            else:
                return float('inf')
            if (i, j) == (row - 1, col - 1):
                res = abs(heights[i][j] - last)
            else:
                res = max(abs(heights[i][j] - last), min(DFS(i + 1, j, heights[i][j]),
                                                         DFS(i, j + 1, heights[i][j]),
                                                         DFS(i - 1, j, heights[i][j]),
                                                         DFS(i, j - 1, heights[i][j])))
            visited[(i, j)] = 0
            return res

        m = heights[0][0]
        res = DFS(0, 0, m)
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
