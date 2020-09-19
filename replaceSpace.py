class Solution:
    def replaceSpace(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == " ": s[i] = "%20"
        return "".join(s)


if __name__ == "__main__":
    test = Solution()
    ans = test.replaceSpace("We are happy.")
    print(ans)
