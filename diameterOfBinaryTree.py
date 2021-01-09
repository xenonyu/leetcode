from handleInput import TreeNode, deserialize


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0

        def recur(root: TreeNode):
            if not root: return 0
            left, right = 0, 0
            left = recur(root.left)
            right = recur(root.right)
            maxLen = max(left, right) + 1
            self.res = max(self.res, left + right)
            return maxLen

        recur(root)
        return self.res


if __name__ == '__main__':
    test = Solution()
    inputList = [1, 2, 3, 4, 5]
    root = deserialize(inputList)
    print(test.diameterOfBinaryTree(root))
