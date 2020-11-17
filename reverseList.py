from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def parseListToListNode(self, inputList: List[int]) -> ListNode:
        head = ListNode(None)
        temp = head
        for value in inputList:
            temp.next = ListNode(value)
            temp = temp.next
        return head.next

    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def reverseListII(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p = self.reverseListII(head.next)
        head.next.next = head
        head.next = None
        return p


if __name__ == "__main__":
    test = Solution()
    inputList = [1, 2, 3, 4]
    startNode = test.parseListToListNode(inputList)
    res = test.reverseListII(startNode)
    while res:
        print(str(res.val) + "->", end="")
        res = res.next
