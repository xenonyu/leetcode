# Definition for a binary tree node.
from handleInput import TreeNode, List, parseListToTree


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        while root != None or stack:
            while root:
                stack.append(root)
                root = root.left
            top = stack.pop()
            res.append(top.val)
            root = top.right
        return res


if __name__ == '__main__':
    inputList = [1, None, 2, 3]
    root = parseListToTree(inputList)
    test = Solution()
    print(test.inorderTraversal(root))
