import heapq
from typing import List


# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def parseListToLN(self, inputLists) -> List[ListNode]:
        result = []
        head = ListNode()
        for list in inputLists:
            temp = head
            for i in range(len(list)):
                temp.next = ListNode(list[i])
                temp = temp.next
            result.append(head.next)
        return result

    def mergeKLists(self, lists: List[ListNode]) -> ListNode or bool:
        if not lists or len(lists) == 0:
            return None
        head = ListNode()
        temp = head
        i = len(lists)
        while i:
            if not lists[i - 1]:
                lists.pop(i - 1)
            i = i - 1
        while lists:
            lists.sort(key=lambda x: x.val)
            temp.next = ListNode(lists[0].val)
            temp = temp.next
            lists[0] = lists[0].next
            if not lists[0]:
                lists.pop(0)
        return head.next

    def useHeap(self, lists: List[ListNode]) -> ListNode or bool:
        if not lists or not len(lists):
            return None
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next

        dummy = ListNode(0)
        cur = dummy
        while heap:
            tempNode = ListNode(heapq.heappop(heap))
            cur.next = tempNode
            cur = cur.next
        return dummy.next

    def divide_and_conquer(self, lists: List[ListNode]) -> ListNode or bool:
        length = len(lists)

        # 边界情况
        if length == 0:
            return None
        if length == 1:
            return lists[0]

        # 分治
        mid = length // 2
        return self.merge(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:length]))

    def merge(self, node_a, node_b):
        dummy = ListNode(0)
        cursor_a, cursor_b, cursor_res = node_a, node_b, dummy
        while cursor_a and cursor_b:  # 对两个节点的 val 进行判断，直到一方的 next 为空
            if cursor_a.val <= cursor_b.val:
                cursor_res.next = ListNode(cursor_a.val)
                cursor_a = cursor_a.next
            else:
                cursor_res.next = ListNode(cursor_b.val)
                cursor_b = cursor_b.next
            cursor_res = cursor_res.next
        # 有一方的next的为空，就没有比较的必要了，直接把不空的一边加入到结果的 next 上
        if cursor_a:
            cursor_res.next = cursor_a
        if cursor_b:
            cursor_res.next = cursor_b
        return dummy.next


if __name__ == "__main__":
    test = Solution()
    inputList = [[1,4,5],[1,3,4],[2,6]]
    input = test.parseListToLN(inputList)
    resultHead = test.divide_and_conquer(input)
    while resultHead:
        print(resultHead.val, end="")
        resultHead = resultHead.next