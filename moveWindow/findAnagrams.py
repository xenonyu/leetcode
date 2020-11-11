from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res, l, count = [], 0, 0
        sLen, pLen = len(s), len(p)
        if sLen < pLen: return []
        pCounter, window = Counter(p), Counter()
        for r in range(sLen):
            char = s[r]
            if char in pCounter:
                window[char] += 1
                if window[char] == pCounter[char]: count += 1
            while count == len(pCounter):
                # print(l, r)
                if r - l + 1 == pLen: res.append(l)
                char = s[l]
                if char in pCounter:
                    window[char] -= 1
                    if window[char] < pCounter[char]: count -= 1
                l += 1
        return res
