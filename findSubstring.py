from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordsLen, wordLen, sLen, tLen = len(words), len(words[0]), len(s), len(words) * len(words[0])
        res = []
        wordsCounter = Counter(words)
        for start in range(wordLen):
            slow, maxSlow = start, sLen - tLen
            while slow <= maxSlow:
                flag = True
                tempCounter = wordsCounter.copy()
                for fast in range(slow + tLen - wordLen, slow - 1, -wordLen):
                    key = s[fast:fast + wordLen]
                    if tempCounter[key] == 0:
                        flag = False
                        break
                    tempCounter[key] -= 1
                if flag: res.append(slow)
                slow = fast + wordLen
        return res


if __name__ == '__main__':
    inputStrings = "bcabbcaabbccacacbabccacaababcbb"
    inputWords = ["c", "b", "a", "c", "a", "a", "a", "b", "c"]
    test = Solution()
    res = test.findSubstring(s=inputStrings, words=inputWords)
    print(res)
