from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def parseListToTree(inputList: List[int]) -> TreeNode or bool:
    """

    :type inputList: object
    """
    if not inputList:
        return None
    root = TreeNode(inputList[0])

    for i in range(len(inputList)):
        if inputList[i] is None:
            if 2 * i + 1 <= len(inputList):
                inputList.insert(2 * i + 1, None)
            if 2 * i + 2 <= len(inputList):
                inputList.insert(2 * i + 2, None)

    def recur(node: TreeNode, index: int):
        if 2 * index + 1 < len(inputList) and inputList[2 * index + 1] is not None:
            node.left = TreeNode(inputList[2 * index + 1])
            recur(node.left, 2 * index + 1)
        if 2 * index + 2 < len(inputList) and inputList[2 * index + 2] is not None:
            node.right = TreeNode(inputList[2 * index + 2])
            recur(node.right, 2 * index + 2)

    recur(root, 0)
    return root


def parseListToChain(list: List) -> ListNode:
    head = ListNode(None)
    temp = head
    for i in list:
        temp.next = ListNode(i)
        temp = temp.next
    return head.next


def print_by_layer_1(root):
    """
    2. 逐行打印——初级版：
    用line/current_line 控制换行，在入队时候即加入行号信息
    """
    print("逐行打印")
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
