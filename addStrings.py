class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def addhelp(num1, num2, carry):
            if not num1 and not num2:
                if carry == 1:
                    return str(carry)
                else:
                    return ""
            if not num2:
                return num1
            if not num1: return num2
            carry, last = divmod(int(num1[-1]) + int(num2[-1]) + carry, 10)
            return addhelp(num1[:-1], num2[:-1], carry) + str(last)

        return addhelp(num1, num2, 0)


if __name__ == '__main__':
    num1 = "99"
    num2 = "9"
    test = Solution()
    print(test.addStrings(num1, num2))
