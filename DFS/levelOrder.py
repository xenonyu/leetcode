# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def parseListToTree(self, inputList: List[int]) -> TreeNode or bool:
        if not inputList:
            return None
        root = TreeNode(inputList[0])

        def recur(node: TreeNode, index: int):
            if 2 * index + 1 < len(inputList):
                node.left = TreeNode(inputList[2 * index + 1])
                recur(node.left, 2 * index + 1)
            else:
                return
            if 2 * index + 2 < len(inputList):
                node.right = TreeNode(inputList[2 * index + 2])
                recur(node.right, 2 * index + 2)

        recur(root, 0)
        return root

    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, queue = [], deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res

    def leveOrderII(self, root: TreeNode) -> List[list]:
        if not root: return []
        res, queue, layer = [], deque(), 0
        queue.append(root)
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(temp)
        return res

    def leveOrderIII(self, root: TreeNode) -> List[list]:
        if not root: return []
        res, queue, layer = [], deque(), 0
        queue.append(root)
        while queue:
            temp = deque()
            for i in range(len(queue)):
                node = queue.popleft()
                if len(res) % 2 == 0:
                    temp.append(node.val)
                else:
                    temp.appendleft(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(list(temp))
        return res


if __name__ == "__main__":
    test = Solution()
    inputList = [0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8]
    root = test.parseListToTree(inputList)
    print(test.leveOrderII(root))
