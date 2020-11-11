from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len, s2Len = len(s1), len(s2)
        window, s1Counter = Counter(), Counter(s1)
        l, count = 0, 0
        if s1Len > s2Len: return False
        for r in range(s2Len):
            char = s2[r]
            if char in s1Counter:
                window[char] += 1
                if window[char] == s1Counter[char]: count += 1
            while count == len(s1Counter):
                # print(l, r)
                if r - l + 1 == s1Len: return True
                char = s2[l]
                if char in s1Counter:
                    window[char] -= 1
                    if window[char] < s1Counter[char]: count -= 1
                l += 1
        return False
