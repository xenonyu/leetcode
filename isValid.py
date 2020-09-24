class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)

        return not stack

    def isValidRecursion(self, s: str) -> bool:
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        # 如果空，则合法
        if not s: return True
        # 如果长度为奇数，或者起始为右侧括号，则不合法
        if len(s) % 2 or s[0] not in pairs: return False
        # 循环找到对应的右侧括号
        count = 1
        for i in range(1, len(s)):
            # 找到相同类型右括号+1
            if s[i] == s[0]: count += 1
            # 找到相同类型左括号-1
            if pairs[s[0]] == s[i]: count -= 1
            # 如果为0 则找到了，递归判断合法括号内部和右侧是否合法
            # s[0] ----- s[i] -----
            # 判断'--'部分是否合法
            if count == 0: return self.isValidRecursion(s[1:i]) and self.isValidRecursion(s[i + 1:])
        return False


if __name__ == '__main__':
    test = Solution()
    inputStr = "(())"
    print(test.isValidRecursion(inputStr))
