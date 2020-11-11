from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        length = len(s)
        counter = Counter(t)
        window = Counter()
        res, minLen = "", float('inf')
        count = 0
        for r in range(length):
            char = s[r]
            if char in counter:
                window[char] += 1
                if window[char] == counter[char]: count += 1
            while count == len(counter):
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    res = s[l: r + 1]
                char = s[l]
                if char in counter:
                    window[char] -= 1
                    if window[char] < counter[char]:
                        count -= 1
                l += 1
        return res


if __name__ == '__main__':
    s = "cabwefgewcwaefgcf"
    t = "cae"
    test = Solution()
    print(test.minWindow(s, t))
