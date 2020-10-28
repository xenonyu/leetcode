# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def preTraverse(preStart, preEnd, inStart, inEnd):
            if preStart > preEnd or inStart > inEnd: return
            # print(preStart, preEnd)
            root = TreeNode(preorder[preStart])
            inRoot = inorder.index(root.val)
            numsLeft = inRoot - inStart
            root.left = preTraverse(preStart + 1, preStart + numsLeft, inStart, inRoot - 1)
            root.right = preTraverse(preStart + numsLeft + 1, preEnd, inRoot + 1, inEnd)
            return root

        return preTraverse(0, len(preorder) - 1, 0, len(inorder) - 1)
