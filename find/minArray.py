from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            mid = (i + j) // 2
            if numbers[mid] < numbers[j]:
                j = mid
            elif numbers[mid] > numbers[j]:
                i = mid + 1
            else:
                return min(numbers[i:j])
        return numbers[i]


if __name__ == '__main__':
    inputList = [1, 3, 5]
    test = Solution()
    res = test.minArray(inputList)
    print(res)