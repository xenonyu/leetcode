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

    '''
        翻转head后到tail的区间
    '''
    def reverseGroup(self, head: ListNode, tail: ListNode):
        tailNext = tail.next
        pre = head
        cur = head.next
        while cur != tailNext:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        head.next.next = tailNext
        head.next = tail

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        dummy = ListNode(None)
        dummy.next = head
        cur = dummy
        while True:
            tail = cur
            i = k
            while i and tail:
                tail = tail.next
                i = i - 1
            if not tail:
                return dummy.next
            self.reverseGroup(cur, tail)
            i = k
            while i:
                cur = cur.next
                i -= 1
        return dummy.next


if __name__ == "__main__":
    test = Solution()
    inputList =[1, 2, 3, 4, 5]
    k = 2
    startNode = test.parseListToListNode(inputList)
    startNode = test.reverseKGroup(startNode, k)

    while startNode:
        print(str(startNode.val)+"->", end="")
        startNode = startNode.next