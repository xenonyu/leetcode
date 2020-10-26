from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(begin, curCan, resume):
            if resume < 0: return
            for i in range(begin, len(candidates)):
                if i - 1 >= begin and candidates[i] == candidates[i - 1]: continue
                n = candidates[i]
                if resume == n:
                    res.append(curCan + [n])
                elif resume > candidates[i]:
                    dfs(i + 1, curCan + [n], resume - n)

        candidates.sort()
        dfs(0, [], target)
        return res


if __name__ == '__main__':
    test = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    res = test.combinationSum2(candidates, target)
    print(res)
