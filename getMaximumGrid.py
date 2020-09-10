from typing import List


class Solution:
    def __init__(self):
        self.values = []

    def getMaximumGold(self, gold: List[List[int]]) -> int:
        col, row = len(gold[0]), len(gold)

        def DFS(i, j, value, col, row):
            canGoOn = False
            for i, j in zip((i - 1, i + 1, i, i), (j, j, j - 1, j + 1)):
                if 0 <= i < row and 0 <= j < col and gold[i][j]:
                    currGold = gold[i][j]
                    gold[i][j] = 0
                    DFS(i, j, value + currGold, col, row)
                    gold[i][j] = currGold
                    canGoOn = True
            if not canGoOn:
                self.values.append(value)


        for i in range(row):
            for j in range(col):
                DFS(i, j, 0, col, row)
        return max(self.values)


def main():
    gold: List[List[int]] = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
    test = Solution()
    print(test.getMaximumGold(gold))


if __name__ == '__main__':
    main()
