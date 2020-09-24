class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if not haystack: return -1
        slow, fast = 0, 0
        while fast < len(haystack):
            if haystack[fast] == needle[fast - slow]:
                if fast - slow == len(needle) - 1: return slow
                fast += 1
                continue
            slow = slow + 1
            fast = slow
        return -1


if __name__ == '__main__':
    test = Solution()
    haystack = "mississippi"
    needle = "issip"
    res = test.strStr(haystack, needle)
    print(res)
