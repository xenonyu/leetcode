import threading
from typing import Callable


class Foo:
    def __init__(self):
        self.firstJobDone = threading.Lock()
        self.secondJobDone = threading.Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstJobDone.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.firstJobDone:
            printSecond()
        self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.secondJobDone:
            printThird()


def printFirst():
    print("first", "")


def printSecond():
    print("second", "")


def printThird():
    print("third", "")


if __name__ == '__main__':
    inputList = [1, 3, 2]
    test = Foo()
    threading.Thread(name="1", target=test.first(printFirst=printFirst)).start()
    threading.Thread(name="2", target=test.third(printThird=printThird)).start()
    threading.Thread(name="3", target=test.second(printSecond=printSecond)).start()
