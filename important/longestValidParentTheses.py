class Solution:
    def longestValidParentheses(self, s: str) -> int:
        length, ans = len(s), 0
        dp = [0] * length
        for i in range(1, length):
            if s[i] == '(':
                continue
            elif s[i] == ')' and s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2 if i - 2 >= 0 else 2
            elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                if i - dp[i - 1] - 2 >= 0:
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                else:
                    dp[i] = dp[i - 1] + 2
            ans = max(ans, dp[i])
        return ans

    def stackImplementation(self, s: str) -> int:
        length, ans, stack = len(s), 0, [-1]
        for i in range(length):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack: stack.append(i)
                ans = max(ans, i - stack[-1])
        return ans


if __name__ == '__main__':
    inputString = "(()))())("
    test = Solution()
    print(test.stackImplementation(inputString))
    print(test.longestValidParentheses(inputString))
