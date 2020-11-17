from handleInput import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = {}

        def check(i, j, k):
            if i == 1 and j == 1 and k == 0:
                print()
            if board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            visited[(i, j)] = True
            res = False
            for dx, dy in directions:
                if (i + dx, j + dy) not in visited and 0 <= i + dx < len(board) and 0 <= j + dy < len(board[0]):
                    nextStep = (i + dx, j + dy)
                    res = check(*nextStep, k + 1)
                    if res == True: break
            del visited[(i, j)]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if check(i, j, 0) == True:
                    return True
        return False


if __name__ == '__main__':
    inputBoard = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    word = "AAB"
    test = Solution()
    print(test.exist(inputBoard, word))
