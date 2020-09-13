class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(i, dic[s[j]])  # 更新左指针 i
            dic[s[j]] = j  # 哈希表记录
            res = max(res, j - i)  # 更新结果
        return res


if __name__ == "__main__":
    test = Solution()
    inputStr = "abcabcbbdfafadf"
    res = test.lengthOfLongestSubstring(inputStr)
    print(res)
