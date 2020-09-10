class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        nums = 0
        for i in range(len(s)):
            nums = nums + ord(s[i]) - ord('O')
            if nums == 0:
                ans = ans + 1
        return ans


class Stack(object):
    def __init__(self):
        """创建空列表"""
        self.__list = []

    def isEmpty(self):
        """判断是否为空"""
        return self.__list == []

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        if self.isEmpty():
            return
        return self.__list.pop()

    def top(self):
        if self.isEmpty():
            return
        return self.__list[-1]

    def empty(self):
        self.__list = []


if __name__ == '__main__':
    test = Solution()
    print(test.balancedStringSplit('LRLLLRRR'))