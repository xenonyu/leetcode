from handleInput import parseListToTree, print_by_layer_1


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.x, self.y, self.pre = None, None, None

        def inOrderTraverse(root: TreeNode):
            if root is None: return
            inOrderTraverse(root.left)
            if self.pre and root.val < self.pre.val:
                self.y = root
                if self.x is None: self.x = self.pre
            self.pre = root
            inOrderTraverse(root.right)

        inOrderTraverse(root)
        self.x.val, self.y.val = self.y.val, self.x.val


if __name__ == '__main__':
    inputList = [5, 3, 9, -2147483648, 2]
    root = parseListToTree(inputList)
    # print_by_layer_1(root)
    test = Solution()
    test.recoverTree(root)
    print_by_layer_1(root)
