from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        ans = []
        s = list(s)

        def DFS(x):
            if x == len(s) - 1:
                ans.append("".join(s))
                return
            dic = set()
            for i in range(x, len(s)):
                if s[i] in dic: continue
                dic.add(s[i])
                s[i], s[x] = s[x], s[i]
                DFS(x + 1)
                s[i], s[x] = s[x], s[i]

        DFS(0)
        return ans


if __name__ == "__main__":
    inputStr = "abc"
    test = Solution()
    ans = test.permutation(inputStr)
    print(ans)
