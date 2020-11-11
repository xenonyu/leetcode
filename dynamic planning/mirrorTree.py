from typing import NoReturn, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorBTree(self, root: TreeNode) -> NoReturn:
        left = root.left
        right = root.right
        root.left = right
        root.right = left
        self.mirrorBTree(root.right)
        self.mirrorBTree(root.right)

    def moreThanHalf(self, input: List):
        keyDict = {}
        length = len(input)
        for i in input:
            keyDict[i] = keyDict.get(i, 0) + 1
            if keyDict.get(i, 0) >= length // 2: return i
        return -1

    def uglyNum(self, n):
        keyDict = {1: True, 2: True, 3: True, 4: True, 5: True}

        def recur(n):
            if n in keyDict: return keyDict[n]
            if n % 2:
                res = recur(n // 2)
                keyDict[n] = res
                return res
            elif n % 3:
                res = recur(n // 3)
                keyDict[n] = res
                return res
            elif n % 5:
                res = recur(n // 5)
                keyDict[n] = res
                return res
            keyDict[n] = False
            return False

        num, count = 1, 0
        while True:
            if recur(num) == True: count += 1
            if count == n: break
            num += 1
        return num

    def uglyNumII(self, n):
        dp = {1: True}
        num, count = 2, 1
        while count < n:
            if not num % 2:
                dp[num] = dp[num // 2]
            elif not num % 3:
                dp[num] = dp[num // 3]
            elif not num % 5:
                dp[num] = dp[num // 5]
            else:
                dp[num] = False
            if dp[num]: count += 1
            num += 1
        return num


if __name__ == '__main__':
    test = Solution()
    num = 20
    res = test.uglyNumII(num)
    res2 = test.uglyNum(num)
    print(res, res2)
