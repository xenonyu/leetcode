import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        h, w = len(heights), len(heights[0])
        preStepOrder = []
        stepMap = {}
        heapq.heapify(preStepOrder)
        if h <= 1 and w <= 1: return 0
        pathMap = []
        row, col, maxEnergy, res = 0, 0, 0, 0
        while row < h and col < w:
            pathMap.append([row, col])
            # distance,r, c
            for move in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                target = [row + move[0], col + move[1]]
                if 0 <= target[0] < h and 0 <= target[1] < w and not target in pathMap:
                    d = abs(heights[target[0]][target[1]] - heights[row][col])
                    if not stepMap.get(d):
                        stepMap[d] = [target]
                    else:
                        stepMap[d].append(target)
                    heapq.heappush(preStepOrder, d)
            nextd = heapq.heappop(preStepOrder)
            res = max(res, nextd)
            nextStep = stepMap[nextd].pop()
            # print(nextStep[1]==h-1, w-1==nextStep[2])
            if nextStep[0] == h - 1 and nextStep[1] == w - 1: return res
            row, col = nextStep
        return res


if __name__ == '__main__':
    heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    test = Solution()
    res = test.minimumEffortPath(heights)
    print(res)
