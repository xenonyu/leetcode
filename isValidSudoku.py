from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, columns, boxs = [{} for _ in range(9)], [{} for _ in range(9)], [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.': continue
                if columns[j].get(num, 0):
                    return False
                else:
                    columns[j][num] = 1
                if rows[i].get(num, 0):
                    return False
                else:
                    rows[i][num] = 1
                if boxs[(i // 3) * 3 + j // 3].get(num, 0):
                    return False
                else:
                    boxs[(i // 3) * 3 + j // 3][num] = 1
        return True


if __name__ == '__main__':
    inputList = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    test = Solution()
    res = test.isValidSudoku(inputList)
    print(res)
