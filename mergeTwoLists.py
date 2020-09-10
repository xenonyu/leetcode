from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        D = ListNode()
        temp = D
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 if l1 else l2
        return D.next

    def recursion(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            if l1.val < l2.val:
                l1.next = self.recursion(l1.next, l2)
                return l1
            else:
                l2.next = self.recursion(l1, l2.next)
                return l2


if __name__ == "__main__":
    a: ListNode = ListNode(0)
    b: ListNode = ListNode(2)
    c: ListNode = ListNode(4)
    A: ListNode = ListNode(1)
    B: ListNode = ListNode(3)
    C: ListNode = ListNode(5)
    a.next = b
    b.next = c
    A.next = B
    B.next = C
    test = Solution()
    head = test.recursion(a, A)
    while head:
        print(head.val)
        head = head.next