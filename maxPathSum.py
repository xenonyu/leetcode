# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> float:
        self.ans = -float('inf')

        def postTraversal(root: TreeNode) -> int:
            if root is None: return 0
            leftMax = max(0, postTraversal(root.left))
            rightMax = max(0, postTraversal(root.right))
            self.ans = max(self.ans, leftMax + rightMax + root.val)
            return max(rightMax, leftMax) + root.val

        postTraversal(root)
        return self.ans


if __name__ == '__main__':
    a = [1, 2, 3]
    b = a.index(2)
    print(b)
