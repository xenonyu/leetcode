from handleInput import TreeNode, parseListToTree, draw


class Solution:
    def predecessor(self, root: TreeNode) -> int:
        root = root.left
        while root.right: root = root.right
        return root.val

    def successor(self, root: TreeNode) -> int:
        root = root.right
        while root.left: root = root.left
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root


if __name__ == '__main__':
    inputList = [2, 1]
    target = 2
    root = parseListToTree(inputList)
    # print_by_layer_1(root)
    draw(root)
    test = Solution()
    root = test.deleteNode(root, target)
    # print_by_layer_1(root)
    draw(root)
