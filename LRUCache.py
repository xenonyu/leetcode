class DLinkNode:
    def __init__(self, key=0, val=0):
        self.pre = None
        self.nex = None
        self.key = key
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.nex = self.tail
        self.head.pre = self.tail
        self.tail.nex = self.head
        self.tail.pre = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)
        else:
            node = DLinkNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            if len(self.cache) > self.capacity:
                node = self.deleteTail()
                self.cache.pop(node.key)

    def addToHead(self, node: DLinkNode) -> None:
        node.pre = self.head
        node.nex = self.head.nex
        self.head.nex.pre = node
        self.head.nex = node
        self.cache[node.key] = node

    def deleteTail(self) -> DLinkNode:
        node = self.tail.pre
        self.removeNode(node)
        return node

    def removeNode(self, node: DLinkNode) -> None:
        node.pre.nex = node.nex
        node.nex.pre = node.pre

    def moveToHead(self, node: DLinkNode) -> None:
        self.removeNode(node)
        self.addToHead(node)


if __name__ == '__main__':
    capacity = 2
    test = LRUCache(capacity)
    test.put(1, 1)
    test.put(2, 2)
    print(test.get(1))
    test.put(3, 3)
    print(test.get(2))
