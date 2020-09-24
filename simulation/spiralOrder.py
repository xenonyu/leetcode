from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        low = 0
        high = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while True:
            for i in range(left, right + 1): res.append(matrix[low][i])
            low += 1
            if low > high: break
            for j in range(low, high + 1): res.append(matrix[j][right])
            right -= 1
            if left > right: break
            for i in range(right, left - 1, -1): res.append(matrix[high][i])
            high -= 1
            if low > high: break
            for j in range(high, low - 1, -1): res.append(matrix[j][left])
            left += 1
            if left > right: break

        return res


if __name__ == '__main__':
    test = Solution()
    inputList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = test.spiralOrder(inputList)
    print(result)
