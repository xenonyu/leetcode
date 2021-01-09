from handleInput import TreeNode, deserialize, draw, print_by_layer_1


class Solution:
    def rob(self, root: TreeNode) -> int:
        # res[0] root抢了， res[1] root 没抢
        def dp(root: TreeNode) -> [int, int]:
            if not root: return [0, 0]
            left = dp(root.left)
            right = dp(root.right)
            rob = root.val + left[1] + right[1]
            no_rob = max(left[0], left[1]) + max(right[0], right[1])
            return [rob, no_rob]

        res = dp(root)
        print(res)
        return max(res)


if __name__ == '__main__':
    inputList = [3, 2, 3, None, 3, None, 1]
    root = deserialize(inputList)
    draw(root)
    print_by_layer_1(root)
    test = Solution()
    print(test.rob(root))
