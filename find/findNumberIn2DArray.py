from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix) - 1
        while i < len(matrix[0]) and j:
            if matrix[j][i] == target:
                return True
            elif matrix[j][i] < target:
                i += 1
            else:
                j -= 1
        return False


if __name__ == '__main__':
    test = Solution()
    inputList = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 5
    res = test.findNumberIn2DArray(matrix=inputList, target=target)
    print(res)