from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def parseListToTree(self, inputList: List[int]) -> TreeNode or None:
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

    def print_by_layer_1(self, root):
        '''
        2. 逐行打印——初级版：
        用line/current_line 控制换行，在入队时候即加入行号信息
        '''
        if not root:
            return
        queue = []  #
        current_line = 0
        queue.append([current_line, root])
        while len(queue) > 0:
            line, node = queue.pop(0)
            # 核心判断：是否换行
            if line != current_line:
                print()  # 不同时换行，print()函数默认end=“\n”
                current_line = line
            print(node.val, end=" ")
            if node.left:
                queue.append([line + 1, node.left])  # 将本节点的行号和左子节点入队
            if node.right:
                queue.append([line + 1, node.right])  # 将本节点的行号和右子节点入队
        print()

    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(rootLeft: TreeNode, rootRight: TreeNode) -> bool:
            if not rootLeft and not rootRight:
                return True
            return bool(rootLeft and rootRight and
                        rootLeft.val == rootRight.val and
                        isMirror(rootLeft.left, rootRight.right) and
                        isMirror(rootLeft.right, rootRight.left))

        return not root or isMirror(root.left, root.right)


if __name__ == "__main__":
    test = Solution()
    inputList = [1, 2, 2, 3, 4, 4, 3]
    root = test.parseListToTree(inputList)
    test.print_by_layer_1(root)
    print(test.isSymmetric(root))
