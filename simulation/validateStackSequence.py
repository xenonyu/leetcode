from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        temp = []
        for i in range(len(pushed)):
            temp.append(pushed[i])
            while temp and temp[-1] == popped[j]:
                j += 1
                temp.pop()
        return not temp


if __name__ == '__main__':
    pushed = [1, 0]
    popped = [1, 0]
    test = Solution()
    res = test.validateStackSequences(pushed, popped)
    print(res)
