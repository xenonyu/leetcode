from typing import List

from handleInput import deserialize, print_by_layer_1


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

    def pathSumII(self, root: TreeNode, sum: int):
        def recur(root: TreeNode, preSum):
            if not root: return
            curSum = preSum + root.val
            self.ans += hashMap.get(curSum - sum, 0)
            hashMap[curSum] = hashMap.get(curSum, 0) + 1
            recur(root.left, curSum)
            recur(root.right, curSum)
            hashMap[curSum] -= 1

        hashMap = {0: 1}
        self.ans = 0
        recur(root, 0)
        return self.ans


if __name__ == "__main__":
    inputList = [1, -2, -3, 1, 3, -2, None, -1]
    test = Solution()
    root = deserialize(inputList)
    print_by_layer_1(root)
    res = test.pathSumII(root, 2)
    print(res)
