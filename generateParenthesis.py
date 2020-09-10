from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        if not n:
            return []
        def recursion(countLeft: int, result: str) -> None:
            if countLeft == n:
                for i in range(2 * n - len(result)):
                    result = result + ")"
                results.append(result)
                return
            recursion(countLeft+1, result + "(")
            if len(result) < 2 * countLeft:
                recursion(countLeft, result + ")")
            return
        recursion(0, "")
        return results

    def gpBackTrack(self, n: int) -> List[str]:
        if not n:
            return []
        ans = []

        def backTrack(S, nLeft: int, nRight: int) -> None:
            if 2 * n == len(S):
                ans.append("".join(S))
                return
            if nLeft < n:
                S.append("(")
                backTrack(S, nLeft+1, nRight)
                S.pop()
            if nLeft > nRight:
                S.append(")")
                backTrack(S, nLeft, nRight+1)
                S.pop()
        backTrack([], 0, 0)
        return ans


if __name__ == "__main__":
    test = Solution()
    n = 3
    print(test.gpBackTrack(3))