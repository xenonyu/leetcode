from typing import List

from handleInput import parseListToTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []

        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, sum)
        return res


if __name__ == "__main__":
    inputList = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    test = Solution()
    root = parseListToTree(inputList)
    # print_by_layer_1(root)
    res = test.pathSum(root, 22)
    print(res)
