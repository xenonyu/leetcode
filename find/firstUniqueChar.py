import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = collections.OrderedDict()
        for c in s:
            dic[c] = not c in dic

        for k, v in dic.items():
            if v: return k
        return ' '


if __name__ == '__main__':
    test = Solution()
    inputStr = "leetcode"
    res = test.firstUniqChar(inputStr)
    print(res)