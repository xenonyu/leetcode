from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        if not strs: return ""
        print(zip(*strs))
        ss = list(map(set, zip(*strs)))
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res


if __name__ == '__main__':
    test = Solution()
    strs = ["aa", "a"]
    print(test.longestCommonPrefix(strs))