from typing import List


class ListNode:
    def __init__(self, x):
        self.next = None
        self.val = x


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        D: ListNode = ListNode(0)
        D.next = head
        first = D
        end = D
        for _ in range(n + 1):
            end = end.next
        while end:
            first = first.next
            end = end.next
        first.next = first.next.next
        return D.next

    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     D: ListNode = ListNode(0)
    #     D.next = head
    #     count = 0
    #     temp = D
    #     while temp:
    #         count += 1
    #         temp = temp.next
    #     temp = D
    #     for _ in range(count - n - 1):
    #         temp = temp.next
    #     temp.next = temp.next.next
    #     return D.next


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    # d = ListNode(4)
    # e = ListNode(5)
    a.next = b
    b.next = c
    # c.next = d
    # d.next = e
    test: Solution = Solution()
    head = test.removeNthFromEnd(a, 3)
    while head:
        print(head.val)
        head = head.next