import os


def minStr(string: str) -> int:
    slow = 0
    res = 1
    for fast in range(1, len(string)):
        if string[fast] == string[slow]:
            slow += 1
        else:
            res = fast + 1
            slow = 0
    return res


a = os.urandom(3333)
a *= 2
print(minStr(str(a)))
