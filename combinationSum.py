from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(begin, use, remain):
            if remain < 0: return
            for i in range(begin, len(candidates)):
                n = candidates[i]
                if n == remain:
                    res.append(use + [n])
                elif n < remain:
                    dfs(i, use + [n], remain - n)
        candidates.sort()
        use = []
        res = []
        dfs(0, use, target)
        return res


if __name__ == '__main__':
    test = Solution()
    candidates, target = [2, 7, 6, 3, 5, 1], 9
    print(test.combinationSum(candidates, target))
