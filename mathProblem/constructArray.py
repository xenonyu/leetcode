from typing import List


class Solution:
    def constructArray(self, a: List[int]) -> List[int]:
        temp, res = 1, [1] * len(a)
        for i in range(1, len(a)):
            res[i] = res[i - 1] * a[i - 1]
        for i in range(len(a) - 2, -1, -1):
            temp = temp * a[i + 1]
            res[i] *= temp

        return res


if __name__ == '__main__':
    test = Solution()
    inputList = [1, 2, 3, 4, 5]
    result = test.constructArray(inputList)
    print(result)
