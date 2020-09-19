from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        def DFS(x: int):
            if x == n:
                s = "".join(num[self.start:])
                res.append(s)
                if self.nine == n - self.start: self.start -= 1
                return
            for i in range(0, 10):
                num[x] = str(i)
                if i == 9: self.nine += 1
                DFS(x + 1)
            self.nine -= 1

        self.start = n - 1
        self.nine = 0
        res = []
        num = ['0'] * n
        DFS(0)
        res.pop(0)
        return res


if __name__ == "__main__":
    test = Solution()
    ans = test.printNumbers(3)
    print(ans)
