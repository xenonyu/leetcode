from handleInput import TreeNode, deserialize


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inOrder(root):
            if not root: return True
            left = inOrder(root.left)
            if self.pre >= root.val: return False
            self.pre = root.val
            right = inOrder(root.right)
            return left and right

        self.pre = float('-inf')
        self.res = True
        self.res = inOrder(root)
        return self.res


if __name__ == '__main__':
    inputList = [5, 3, 8, None, None, 7, 9]
    root = deserialize(inputList)
    test = Solution()
    print(test.isValidBST(root))
