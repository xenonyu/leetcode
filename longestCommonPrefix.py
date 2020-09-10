from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        common = ""
        lenStrs = len(strs)
        for i in range(len(strs[0])):
            for j in range(lenStrs -1):
                if strs[j][i] != strs[j + 1][i]:
                    break
                common = common + strs[j][i]
        return common


if __name__ == '__main__':
    test = Solution()
    strs = ["flower","flow","flight"]
    print(test.longestCommonPrefix(strs))