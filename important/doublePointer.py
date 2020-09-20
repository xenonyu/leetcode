from handleInput import ListNode, parseListToChain


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        preHead = ListNode(None)
        preHead.next = head
        first = preHead
        second = head
        while second and second.val != val:
            first, second = second, second.next
        if second: first.next = second.next
        return preHead.next


if __name__ == '__main__':
    inputList = [4, 5, 1, 9]
    val = 5
    head = parseListToChain(inputList)
    test = Solution()
    head = test.deleteNode(head, val)
    while (head):
        print(head.val)
        head = head.next
