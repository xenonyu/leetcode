from typing import List

from isValidSudoku import Solution as isValidSudoku


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, columns, boxs = [[set(range(1, 10)) for _ in range(9)] for _ in range(3)]
        bidx = lambda i, j: i // 3 * 3 + j // 3
        empty = []
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    empty.append((i, j))
                else:
                    num = int(num)
                    rows[i].remove(num)
                    columns[j].remove(num)
                    boxs[bidx(i, j)].remove(num)
        n = len(empty)

        def backTrack(position):
            if position == n: return True
            i, j = empty[position]
            for candidate in rows[i] & columns[j] & boxs[bidx(i, j)]:
                rows[i].remove(candidate)
                columns[j].remove(candidate)
                boxs[bidx(i, j)].remove(candidate)
                board[i][j] = str(candidate)
                if backTrack(position + 1): return True
                rows[i].add(candidate)
                columns[j].add(candidate)
                boxs[bidx(i, j)].add(candidate)
            return False

        backTrack(0)


if __name__ == '__main__':
    test = Solution()
    a = set(range(1, 9))
    a.remove(3)
    inputBoard = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                  [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                  ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                  [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    test.solveSudoku(inputBoard)
    tester = isValidSudoku()
    print(tester.isValidSudoku(inputBoard))
