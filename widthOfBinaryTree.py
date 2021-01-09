from handleInput import TreeNode, deserialize, draw, print_by_layer_1


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = [(root, 0, 0)]
        cur_depth = left = ans = 0
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth + 1, pos * 2))
                queue.append((node.right, depth + 1, pos * 2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)

        return ans


if __name__ == '__main__':
    inputList = [1, 3, 2, 5, 3, None, 9]
    root = deserialize(inputList)
    draw(root)
    print_by_layer_1(root)
    test = Solution()
    print(test.widthOfBinaryTree(root))
