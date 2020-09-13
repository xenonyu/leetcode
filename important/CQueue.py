class CQueue:
    def __init__(self):
        self.positive = []
        self.reverse = []

    def appendTail(self, value: int) -> None:
        self.positive.append(value)

    def deleteHead(self) -> int:
        if self.reverse:
            return self.reverse.pop()
        elif not self.positive:
            return -1
        else:
            while self.positive:
                self.reverse.append(self.positive.pop())
            return self.reverse.pop()


obj = CQueue()
value = 1
obj.appendTail(value)
result = obj.deleteHead()
print(result)
