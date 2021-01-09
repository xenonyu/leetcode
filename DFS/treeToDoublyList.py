from handleInput import deserialize, print_by_layer_1


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node' or None:

        def DFS(cur):
            cur = cur
            if not cur: return
            DFS(cur.left)
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = cur
            self.pre = cur
            DFS(cur.right)

        self.head = None
        self.pre = None
        DFS(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


if __name__ == '__main__':
    inputList = [4, 2, 5, 1, 3]
    root = deserialize(inputList)
    print_by_layer_1(root)
    test = Solution()
    head = test.treeToDoublyList(root)
    print(1)
