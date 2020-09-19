import handleInput


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestorForBTree(self, root: TreeNode, p: int, q: int) -> TreeNode:
        if root.val < p and root.val < q:
            return self.lowestCommonAncestorForBTree(root.right, p, q)
        if root.val > p and root.val > q:
            return self.lowestCommonAncestorForBTree(root.left, p, q)
        return root

    def lowestCommonAncestorForTree(self, root, p: int, q: int):
        def DFS(cur: TreeNode):
            if not cur or cur.val == p or cur.val == q: return cur
            left = DFS(cur.left)
            right = DFS(cur.right)
            if not left: return right
            if not right: return left
            return cur

        return DFS(root)


if __name__ == '__main__':
    test = Solution()
    inputList, p, q = [-1, 0, 3, -2, 4, None, None, 8], 8, 4
    root = handleInput.parseListToTree(inputList)
    handleInput.print_by_layer_1(root)
    ans = test.lowestCommonAncestorForTree(root, p, q)
    print("answer is: ", ans.val)
