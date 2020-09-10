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

    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            temp = cur.next
            cur.next = cur.next.next
            temp.next = cur.next.next
            cur.next.next = temp
            cur = cur.next.next
        return dummy.next


if __name__ == '__main__':
    test = Solution()
    inputList = [1,2,3,4]
    result = test.swapPairs(test.parseListToListNode(inputList))
    while result:
        print(result.val)
        result = result.next