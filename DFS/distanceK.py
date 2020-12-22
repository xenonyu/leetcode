from handleInput import TreeNode, List, parseListToTree, draw


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        res = []

        def getSubAns(node, l):
            if not node: return
            if l == 0:
                res.append(node.val)
                return
            getSubAns(node.left, l - 1)
            getSubAns(node.right, l - 1)

        def DFS(node):
            if not node: return -1
            if node == target:
                getSubAns(node, K)
                return 1
            else:
                L, R = DFS(node.left), DFS(node.right)
                if L != -1:
                    if L == K: res.append(node.val)
                    getSubAns(node.right, K - L - 1)
                    return L + 1
                elif R != -1:
                    if R == K: res.append(node.val)
                    getSubAns(node.left, K - R - 1)
                    return R + 1
                else:
                    return -1

        DFS(root)
        return res


if __name__ == '__main__':
    inputList = [0, 2, 1, None, None, 3]
    root = parseListToTree(inputList)
    draw(root)
    test = Solution()
    print(test.distanceK(root, target=root.right.left, K=3))
