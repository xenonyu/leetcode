from handleInput import ListNode, parseListToChain, print_chain


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        preHead = ListNode(0)
        preHead.next = head
        temp = preHead
        pos = 0
        for i in range(m - 1):
            temp = temp.next
        pre = temp
        a = pre
        for i in range(n - m + 2):
            temp = temp.next
        after = temp
        cur = pre.next
        for i in range(n - m + 1):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        a.next.next = after
        a.next = cur
        return preHead.next


if __name__ == '__main__':
    inputList = [1, 2, 3, 4, 5]
    head = parseListToChain(inputList)
    m = 2
    n = 4
    test = Solution()
    head = test.reverseBetween(head, m, n)
    print_chain(head)
