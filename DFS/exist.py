from handleInput import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        w, h, l = len(board[0]), len(board), len(word)
        visited = [[False for _ in range(w)] for _ in range(h)]

        # memo = {}
        def DFS(i, j, index):
            if not 0 <= i < h or not 0 <= j < w or visited[i][j] or board[i][j] != word[index]: return False
            if index == l - 1: return True
            visited[i][j] = True
            res = DFS(i + 1, j, index + 1) or DFS(i, j + 1, index + 1) or DFS(i - 1, j, index + 1) or DFS(i, j - 1,
                                                                                                          index + 1)
            visited[i][j] = False
            # memo[(i, j)] = res
            return res

        for i in range(h):
            for j in range(w):
                if DFS(i, j, 0): return True
        # print(memo)
        return False


if __name__ == '__main__':
    board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    word = "AAB"
    test = Solution()
    print(test.exist(board, word))
    # import collections
    a = {}
    print(a.get(1, 0))
